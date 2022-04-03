from django.contrib import admin

from product.models import Customer, Order, Product, Tag

# Register your models here.
admin.site.register(Customer)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Product)
