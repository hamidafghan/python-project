
import django


from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('products/', views.products, name="products"),
    path('customers/', views.customers, name="customers"),
    path('customers/create/', views.customer_create, name="customers.create"),
    path('customers/<int:id>/', views.customer, name="customers.show"),
    path('orders/', views.orders, name="orders")
]
