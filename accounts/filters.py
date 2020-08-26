import django_filters
from .models import *


class OrderFilter(django_filters.FilterSet):
    #gte = greater then or equal to
    #lte = lesser then or equal to
    #auto build up
    start_date = django_filters.DateFilter(field_name = 'date_created', lookup_expr = 'gte')
    end_date = django_filters.DateFilter(field_name = 'date_created', lookup_expr = 'lte')
    #icontains will accept character match,
    note = django_filters.CharFilter(field_name = 'note', lookup_expr = 'icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created'] # exclude these 2 in search line.
