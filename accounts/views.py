from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# Create your views here.
from .models import *
from .forms import *
from .filters import *
from .decorators import *


# use decorators to insert an extra function when home function is used
@login_required(login_url = 'login')
@admin_only
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


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer', ])
def userPage(request):
    orders = request.user.customer.order_set.all()
    print('ORDERS:', orders)
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()  # this status is the database columns
    context = {'orders': orders, 'delivered': delivered, 'pending': pending, 'total_orders': total_orders}
    return render(request, 'accounts/user.html', context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer', ])
def accountSetting(request):
    customer = request.user.customer
    form = CustomerForm(instance = customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance = customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'accounts/account_settings.html', context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin', ])
def product(request):
    products = Product.objects.all()

    return render(request, 'accounts/product.html', {'products': products})  # we pass templates to products.html


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin', ])
def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    # when get request is received , the orders will be filtered to myFilter.qs

    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter': myFilter}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin', ])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra = 5)
    # fields is required coliums to be displayed
    customer = Customer.objects.get(id = pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)
    # form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)  # is a super handy way to do form saving
        formset = OrderFormSet(request.POST, instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin', ])
def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order)  # instance to indicate which order
    # start dicision making, when action='' redirect post to this url
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)  # and save to that order
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin', ])
def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)


@unauthenticated_user
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        loginCheck = authenticate(request, username = username, password = password)
        if loginCheck is not None:
            login(request, loginCheck)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect.')
    context = {}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
