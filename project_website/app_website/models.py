from ast import Num
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

#####----------------Validator Functions to check validation in models------------------------#####


# def valid_function(value):
#     if "+91" in value:
#         return value

#     else:
#         raise ValidationError('Only indian mobile number accepted.')







#####---------------==================================================------------------------#####



 #category model
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null= True)
    category_name   = models.CharField(max_length=50, unique=True, db_index=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255, blank=True)
    cat_image       = models.ImageField(upload_to='photos/category', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('category_name',)
        managed = True
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self)-> str:
        return self.category_name

#subcategory model
class Subcategory(models.Model):
    category_name   =    models.ForeignKey(Category, on_delete=models.CASCADE)
    name   = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255, blank=True)
    subcat_image       = models.ImageField(upload_to='photos/subcategory', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        managed = True
        db_table = 'sub_categories'
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self)-> str:
        return self.name + " -- " + self.category_name.category_name

#child category model
class Childcategory(models.Model):
    id = models.AutoField(primary_key=True)
    category_name   =    models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name   =    models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name   = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255, blank=True)
    child_image       = models.ImageField(upload_to='photos/childcategory', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-name',)
        managed = True
        db_table = 'child_categories'
        verbose_name = 'childcategory'
        verbose_name_plural = 'childcategories'

    def __str__(self)-> str:
        return self.name



#products
class Product(models.Model):

    category_name   =    models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name   =    models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name   = models.CharField(max_length=50, unique=True)
    slug            = models.SlugField(max_length=100, unique=True)
    description     = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image       = models.ImageField(upload_to='photos/products', blank=True)
    seller_id = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255,null=True)
    created = models.DateTimeField(auto_now_add=True, null=True , blank=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'products'

    # def __str__(self)-> str:
    #     return self.name



class Cart(models.Model):
    # product=models.OneToOneField(Product,on_delete=models.DO_NOTHING,related_name='product')
    # product_code = models.CharField(max_length=255,null=True)
    product_code = models.ForeignKey(Product , on_delete=models.DO_NOTHING,null= True)
    seller_id = models.CharField(max_length=255,null=True)
    price = models.CharField(max_length=255,null=True)
    quantity=models.BigIntegerField(max_length=100,null=True)
    buyer_mobile = models.CharField(max_length=255)
    total_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cart'





class Users(models.Model):

    mobile = models.BigIntegerField()
    otp = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    password=models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'users'


class Orders(models.Model):

    buyer_mobile=models.CharField(max_length=255)
    seller_id=models.CharField(max_length=255)
    order_id=models.CharField(max_length=255)
    order_status=models.IntegerField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True,blank=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table="order_details"
