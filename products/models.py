from email.policy import default
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    in_stock = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    