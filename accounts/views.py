from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    totcust=customers.count()
    totorder=orders.count()
    delivered=orders.filter(status='delivered').count()
    pending=orders.filter(status='pending').count()
    
    context={'orders':orders,'customers':customers,'totorder':totorder,'delivered':delivered,'pending':pending}
    return render(request,'accounts/home.html',context)
def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})
def customers(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    order_count=orders.count()
    context={'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'accounts/customers.html',context)
    