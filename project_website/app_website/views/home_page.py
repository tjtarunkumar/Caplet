from itertools import count
from multiprocessing import context
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect, render
from django.db import connection


# from project_website.models import Products
from ..models import Category, Subcategory,Product , Cart

import json

def index(request, category_slug=None):
    # return HttpResponse("Hello, world. You're at the polls index.")
    session=request.session.get('mobile_number')
    # print("session value of user's mobile number is "+session)
    category = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    products=Product.objects.all()
    context = {'categories': categories, subcategories:subcategories , 'session':session ,'products':products}
    return render(request,'app_website/home_body.html', context)

def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
    # Create your views here.

def contact_us(request):
    category = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {'categories': categories, subcategories:subcategories }
    return render(request,'app_website/contact.html',context)

def logout(request):
    del request.session['mobile_number']
    session=request.session.get('mobile_number')
    # print("session value of user's mobile number is "+str(session))
    return redirect('/')

def display():
    print('function executed')