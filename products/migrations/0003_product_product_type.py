# Generated by Django 4.1.2 on 2022-11-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_category_product_is_best_seller_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
