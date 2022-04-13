
import django


from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='dashboard'),
    path('products/', views.products, name="products"),
    path('orders/', views.orders, name="orders"),

    # Customers
    path('customers/', views.customers, name="customers"),
    path('customers/create/', views.customer_create, name="customers.create"),
    path('customers/<int:id>/', views.customer, name="customers.show"),
    path('customers/<int:id>/edit/', views.customer_edit, name="customers.edit"),
    path('customers/<int:id>/delete/',
         views.customer_delete, name="customers.delete")
]
