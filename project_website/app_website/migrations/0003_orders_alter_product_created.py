# Generated by Django 4.1.1 on 2022-09-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
