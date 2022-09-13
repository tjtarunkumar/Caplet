from django.contrib import admin
from .models import Category
from .models import Subcategory
from .models import Childcategory
from .models import Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'cat_image')
admin.site.register(Category, CategoryAdmin)

class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('category_name', 'name', 'slug')
admin.site.register(Subcategory, SubcategoryAdmin)

class ChildcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('category_name', 'subcategory_name', 'name', 'slug')

    
admin.site.register(Childcategory, ChildcategoryAdmin)
admin.site.register(Product) 