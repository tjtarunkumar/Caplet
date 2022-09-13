from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import redirect, render
from ..models import Category, Subcategory,Product
# from ....function_file import * 

def single_page(request,pk):
    # return HttpResponse(pk)
    # try:
        session=request.session.get('mobile_number')
        data=Product.objects.filter(product_code=pk).get()
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        context = {'categories': categories, subcategories:subcategories ,'session':session ,'product':data}
        return render(request,'app_website/single-page.html',context)
    # except:
    #     return JsonResponse({'error':'sorry there was an error.'})

