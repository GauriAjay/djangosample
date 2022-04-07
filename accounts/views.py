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
    notdelivered=orders.filter(status='notdelivered').count()
    
    context={'orders':orders,'customers':customers,'totorder':totorder,'delivered':delivered,'notdelivered':notdelivered}
    return render(request,'accounts/home.html',context)
def products(request):
    products=Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})
def customers(request):
    return render(request,'accounts/customers.html')