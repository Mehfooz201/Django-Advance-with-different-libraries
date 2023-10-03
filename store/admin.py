from django.contrib import admin
from . import models
from django.utils.html import format_html, urlencode
from django.db.models.aggregates import Count, Max, Min, Avg
from django.urls import reverse




#Customization Admin Side of Models
class OrderItemInline(admin.TabularInline):
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'placed_at', 'customer']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    #Auto Fileds for search except displaying all data records if we have 1000 data, it will render from 
    #db it will not good practice our website will be load slowly.
    autocomplete_fields = ['collection']

    #Auto Slug Update
    prepopulated_fields = {
        'slug' : ['title']
    } 

    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price',]
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        else:
            return 'Ok'


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

    search_fields = ['first_name__istartswith', 'last_name__iendswith']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'products_count']

    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection_id' : str(collection.id)
            })
        )
        return format_html('<a href="{}" target="_blank">{}</a>', url, collection.products_count)
        # return format_html('<a href="https://google.com" target="_blank">{}</a>', collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )