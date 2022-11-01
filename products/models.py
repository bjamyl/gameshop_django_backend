from email.policy import default
from xmlrpc.client import Boolean
from django.db import models
from django.forms import BooleanField

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    in_stock = models.BooleanField(default=True)
    is_featured_product = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    category = models.CharField(max_length=200,null=True)
    product_type = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    