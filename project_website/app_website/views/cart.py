from itertools import count
from multiprocessing import context
from django.http import HttpRequest, HttpResponse, JsonResponse,HttpResponseRedirect
from django.conf import settings
from django.shortcuts import redirect, render
from django.db import connection
from django.db.models import Sum
from app_website.middlewares.auth import *

# from project_website.models import Products
from ..models import Category, Subcategory,Product , Cart

import json

@simple_middleware
def cart(request,id):
    session=request.session.get('mobile_number')
    category = None
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    # print(id)
    cart_data=Cart.objects.filter(buyer_mobile=id).values_list('product_code',flat=True)
    data=list(cart_data)
    test_list=list()

    for x in data:
        item=Cart.objects.select_related('product_code').filter(product_code=x,buyer_mobile=id)
        test_list.append(item)
    total_cart_amount=Cart.objects.filter(buyer_mobile=session).aggregate(Sum('total_amount'))
    total_amount=total_cart_amount['total_amount__sum']

    for x in test_list:
        print(x)

    context = {'categories': categories, 'subcategories':subcategories ,'session':session,'product_detail':test_list,'total_amount':total_amount}
    return render(request,'app_website/cart.html',context)




def change_quantity(request):
    Buyer_mobile=request.POST.get('buyer_mobile')
    Product_id=request.POST.get('product_id')
    Quantity=request.POST.get('quantity')

    Cart.objects.filter(buyer_mobile=Buyer_mobile,product_code_id=Product_id).update(quantity=Quantity)
    item=Product.objects.filter(product_code=Product_id).get()
    cart_item=Cart.objects.filter(product_code_id=Product_id,buyer_mobile=Buyer_mobile).get()
    price=item.price
    product_total_amount=(cart_item.quantity*price)
    # print(product_total_amount)
    Cart.objects.filter(buyer_mobile=Buyer_mobile,product_code_id=Product_id).update(total_amount=product_total_amount)

    total_cart_amount=Cart.objects.filter(buyer_mobile=Buyer_mobile).aggregate(Sum('total_amount'))
    # print(total_cart_amount['total_amount__sum'])
    data=total_cart_amount['total_amount__sum']

    return JsonResponse({'total_cart_amount':data})


def delete_product(request):
    Buyer_mobile=request.POST.get('buyer_mobile')
    Product_code=request.POST.get('product_id')

    Cart.objects.filter(buyer_mobile=Buyer_mobile,product_code_id=Product_code).delete()

    return JsonResponse({'status':0})


def cart_count(request):
    buyer_mobile=request.POST.get('buyer_mobile')
    count=Cart.objects.filter(buyer_mobile=buyer_mobile).count()

    return JsonResponse({'count':count})