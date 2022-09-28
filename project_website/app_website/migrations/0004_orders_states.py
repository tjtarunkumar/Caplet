# Generated by Django 4.1.1 on 2022-09-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_website', '0003_orders_alter_product_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_mobile', models.CharField(max_length=255)),
                ('seller_id', models.CharField(max_length=255)),
                ('order_id', models.CharField(max_length=255)),
                ('order_status', models.IntegerField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'order_details',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'states',
            },
        ),
    ]