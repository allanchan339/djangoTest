from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    # connect User&group to Customer table
    user = models.OneToOneField(User, blank = True, null = True, on_delete = models.CASCADE)
    # https://stackoverflow.com/questions/38388423/what-does-on-delete-do-on-django-models
    name = models.CharField(max_length = 200, null = True)
    phone = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)
    profile_pic = models.ImageField(default = 'html-flat.png', null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    # report the name when display in admin panel


class Tag(models.Model):
    name = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name
    # report the name when display in admin panel


class Product(models.Model):
    CATEGORY = (
            ('Indoor', 'Indoor'),
            ('Out Door', 'Out Door'),
            )
    name = models.CharField(max_length = 200, null = True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length = 200, null = True, choices = CATEGORY)
    description = models.CharField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
            ('Pending', 'Pending'),
            ('Out of delivery', 'Out of delivery'),
            ('Delivered', 'Delivered')
            )
    customer = models.ForeignKey(Customer, null = True,
                                 on_delete = models.SET_NULL)  # on_delete is false, which means the
    # parent deleted wont delete for child
    product = models.ForeignKey(Product, null = True, on_delete = models.SET_NULL)
    status = models.CharField(max_length = 200, null = True, choices = STATUS)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    note = models.CharField(max_length = 1000, null = True)

    def __str__(self):
        return f'{self.customer.name} : {self.product.name}'
