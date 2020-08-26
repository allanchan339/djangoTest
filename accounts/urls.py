from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name = 'home'),
        path('product/', views.product, name = 'products'),
        path('customer/<str:pk>/', views.customer, name = 'customer'),
        path('create_order/', views.createOrder, name = 'create_order'),
        path('create_order/<str:pk>/', views.updateOrder, name = 'update_order')
        # pk = primary key
        ]
