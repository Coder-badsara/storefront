from django.contrib import admin
from django.urls import reverse 
from django.utils.html import format_html , urlencode
from django.db.models import Count
from . import models

# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory_status', 'collection']
    list_editable = ['price']
    list_per_page = 10

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 100:
            return 'Low'
        return 'OK'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'order_count']
    list_editable = ['membership']
    list_per_page = 10
    
    @admin.display(ordering = 'order_count')
    def order_count(self, customer):
        url = (reverse('admin:store_order_changelist')
               + '?'
               + urlencode({
                   'customer__id': str(customer.id)
               }))
        return format_html('<a href="{}">{}</a>', url, customer.order_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(order_count = Count('order'))

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer', 'placed_at', 'payment_status']
    ordering = ['-placed_at']
    list_per_page = 20
    
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']
    
    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (reverse('admin:store_product_changelist')
               + '?'
               + urlencode({
                   'collection__id':str(collection.id)
                   }))
        
        return format_html('<a href ="{}">{}</a>',url, collection.product_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(product_count=Count('product'))

admin.site.register(models.Promotion)
admin.site.register(models.OrderItem)
admin.site.register(models.Address)
admin.site.register(models.Cart)
admin.site.register(models.CartItem)