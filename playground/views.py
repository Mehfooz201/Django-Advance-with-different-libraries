from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # query_set = Product.objects.all()
    product = Product.objects.filter(unit_price__gt=(20, 30))

    return render(request, 'hello.html', {'name': 'Mehfooz Ali', 'product': list(product)})
