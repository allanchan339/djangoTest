from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import *


def home(request):
    orders = Order.objects.all()  # django shell function (API)???
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()  # this status is the database columns
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders':
        total_orders, 'delivered': delivered, 'pending': pending}
    # make a dictionary
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()

    return render(request, 'accounts/product.html', {'products': products})  # we pass templates to products.html


def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = OrderForm(request.POST)  # is a super handy way to do form saving
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order) #instance to indicate which order
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order) #and save to that order
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
