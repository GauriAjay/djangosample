from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import OrderForm
from .filters import OrderFilter

# Create your views here.
def registerPage(request):
    context={}
    return render(request,'accounts/register.html',context)
def loginPage(request):
    context={}
    return render(request,'accounts/login.html',context)
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
    myFilter=OrderFilter(request.GET, queryset=orders)
    orders=myFilter.qs
    context={'customer':customer,'orders':orders,'order_count':order_count,'myFilter':myFilter}
    return render(request,'accounts/customers.html',context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)