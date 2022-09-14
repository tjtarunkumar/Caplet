from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.shortcuts import redirect, render
from ..models import Category, Subcategory,Product, Cart



def product_purchase(request):
    # try:
        #Extract all the params sent through POST method.
        Product_code=request.POST.get('product_code')
        User_mobile=request.POST.get('user_mobile')
        Seller_id=request.POST.get('seller_id')
        Price=request.POST.get('price')

        data=Cart.objects.filter(product_code_id=Product_code,buyer_mobile=User_mobile).exists()
        # print(data)
        #Filter out the record to find a record in which a user has already added the same product in the cart and if a record is found already in the table then add the quantity of the product by 1.

        # print('data is cart-->',data)

        if data:
            item=Cart.objects.get(product_code_id=Product_code)
            price=item.price
            total_quantity=item.quantity+1
            price=int(float(price))
            total_quantity=int(total_quantity)
            x=(price * total_quantity)
            Cart.objects.filter(product_code_id=Product_code,buyer_mobile=User_mobile).update(quantity=total_quantity,total_amount=x)
        else:
            cart=Cart()
            cart.product_code_id=Product_code
            cart.buyer_mobile=User_mobile
            cart.seller_id=Seller_id
            cart.price=Price
            cart.total_amount=Price
            cart.quantity=1
            cart.save()

        return JsonResponse({'status':'0'})