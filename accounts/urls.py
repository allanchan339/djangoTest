from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        path('', views.home, name = 'home'),
        path('product/', views.product, name = 'products'),
        path('customer/<str:pk>/', views.customer, name = 'customer'),
        path('create_order/<str:pk>', views.createOrder, name = 'create_order'),
        path('update_order/<str:pk>/', views.updateOrder, name = 'update_order'),
        # pk = primary key
        path('delete_order/<str:pk>/', views.deleteOrder, name = 'delete_order'),
        path('user/', views.userPage, name="user-page"),
        path('register/', views.registerPage, name = 'register'),
        path('login/', views.loginPage, name = 'login'),
        path('logout/', views.logoutUser, name = 'logout'),

        path('account/', views.accountSetting, name = 'account'),

        path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),
             name = 'reset_password'),
        path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name =
                                                                              'accounts/password_reset_sent.html'),
             name = 'password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset.html'),
             name = 'password_reset_confirm'),
        path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name =
                                                                                     'accounts/password_reset_done.html'),
             name = 'password_reset_complete'),
        # 1. Submit email reset pw form
        # 2. Email sent success message
        # 3. Link to pw reset form in email
        # 4. Password successfully changed message

        ]

