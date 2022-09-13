from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import redirect, render
from ..models import *
import random
from django.http import HttpResponseRedirect

    

def login(request):
    try:
        session=request.session.get('mobile_number')
        category = None
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        context = {'categories': categories, 'subcategories':subcategories ,'session':session}
        return render(request,'app_website/login.html',context)

    except:
        return JsonResponse({'status':'Something went wrong.'})

def register(request):
    try:
        category = None
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        context = {'categories': categories, subcategories:subcategories }
        return render(request,'app_website/register.html',context)
    except:
        return JsonResponse({'status':'Something went wrong.'})



# Function to check user email exists or not. This function is used by ajax in login page.
def emailcheck(request):
    if request.method == "POST":
        user_email=request.POST.get('email')
        user_password=request.POST.get('password')
        password=Users.objects.filter(password=user_password).values_list('password', flat=True)
        email=Users.objects.filter(email=user_email).values_list('email', flat=True)
        data1=list(email)
        data2=list(password)
        if (len(data1) and len(data2)) != 0 :
                return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':1})

def otp_generation(request):
    try:
        num = random.randrange(1000,100000)
        # num --> this number will be sent to the user.

        mobile_number=request.POST.get('mobile')

        user_otp=Users.objects.filter(mobile=mobile_number).values_list('otp',flat=True)

        if len(user_otp) != 0:
            Users.objects.filter(mobile=mobile_number).update(otp=num)
        else:
            user=Users()
            user.mobile=mobile_number
            user.otp=num
            user.save()
        return JsonResponse({'status':'ok'})

    except:
        return JsonResponse({'status':'Something went wrong.'})

def otp_verification(request):
    # Here the data sent through ajax is fetched through the request object's properties and then processed further.
    try:
        mobile_number=request.POST.get('mobile')
        otp_number=request.POST.get('otp')

        user_data=Users.objects.values_list('mobile','otp').filter(mobile=mobile_number,otp=otp_number)

        if(len(user_data) == 0):
            # no record found which means otp is incorrect.
            return JsonResponse({'status':0})

        # Record found which means otp is correct.
        request.session['mobile_number']= mobile_number
        # session=request.session.get('mobile_number')
        # print("session value of user's mobile number is "+session)
        return JsonResponse({'status':1})

    except:
        return JsonResponse({'status':'Something went wrong.'})

    