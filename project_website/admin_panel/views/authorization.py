from django.http import HttpRequest, HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import *


from app_website.models import *

# Create your views here.

def login(request):
    return render(request,'admin_panel/login.html')

def user_login_validation(request):
    Email=request.POST.get('email')
    data=Users.objects.filter(email=Email).values()
    if data:
        return JsonResponse({'status':'0'})    
    else:
        return JsonResponse({'status':'1'})


def check_credentials(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    
    data=Users.objects.filter(email=email,password=password).values()
    if data:
        # User is authenticated
        request.session['email']= email

        return JsonResponse({'result':'0'})
    else:
        # User is not authenticated.
        return JsonResponse({'result':'1'})
    