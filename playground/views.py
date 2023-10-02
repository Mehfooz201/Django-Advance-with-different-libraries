from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem, Order
from django.db.models.aggregates import Count, Max, Min, Avg



def say_hello(request):
    products = None
    orders = None
    # query_set = Product.objects.all()
    #Simple Query
    # products = Product.objects.filter(title__icontains='coffee')

    #Compex Queries
    # products = Product.objects.order_by('unit_price')[0:5]

    #Values Queries
    # products = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())

    #Complex Queries Joins
    # orders = Order.objects.select_related('customer').order_by('-placed_at')[0:5]

    #Aggregate Functions
    products = Product.objects.aggregate(Count('description'))

    # print(products)

    context = {
        'name': 'Mehfooz Ali', 
        'products': products,
        'orders' : orders

    }

    return render(request, 'home.html', context)
