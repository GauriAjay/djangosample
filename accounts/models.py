from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=100, null=True)
    mobile= models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=100, null=True)
    date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(('Indoor','Indoor'),
    ('Out door','Out door'))
    name= models.CharField(max_length=100, null=True)
    price= models.FloatField(null=True)
    description= models.CharField(max_length=100, null=True)
    category= models.CharField(max_length=100, null=True,choices=CATEGORY)
    date= models.DateTimeField(auto_now_add=True, null=True)
class Order(models.Model):
    STATUS=(('not yet delivered','not yet deliverd'),
    ('out for delivery','out for delivery'),
    ('delivered','delivered'),
    )
    date= models.DateTimeField(auto_now_add=True, null=True)
    status= models.CharField(max_length=100, null=True)
