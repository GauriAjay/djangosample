from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=100, null=True)
    mobile= models.CharField(max_length=100, null=True)
    email= models.CharField(max_length=100, null=True)
    date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name= models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY=(('Indoor','Indoor'),
    ('Out door','Out door'))
    name= models.CharField(max_length=100, null=True)
    price= models.FloatField(null=True)
    description= models.CharField(max_length=100, null=True,blank=True)
    category= models.CharField(max_length=100, null=True,choices=CATEGORY)
    date= models.DateTimeField(auto_now_add=True, null=True)
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    STATUS=(('notdelivered','notdeliverd'),
    ('out for delivery','out for delivery'),
    ('delivered','delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date= models.DateTimeField(auto_now_add=True, null=True)
    status= models.CharField(max_length=100, null=True,choices=STATUS)
  
