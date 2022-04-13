from django.shortcuts import render, redirect
from product.models import Product, Customer, Order
from .forms import CustomerForm

# Create your views here.


def home(request):
    order_count = Order.objects.count()
    customer_count = Customer.objects.count()
    product_count = Product.objects.count()

    customers = Customer.objects.all().order_by('-id')[:5]
    orders = Order.objects.all().order_by('-id')[:5]
    products = Product.objects.all().order_by('-id')[:5]

    contex = {
        'order_count': order_count,
        'customer_count': customer_count,
        'product_count': product_count,
        'orders': orders,
        'customers': customers,
        'products': products
    }
    return render(request, 'product/home.html', context=contex)


def products(request):
    products = Product.objects.all()

    return render(request, 'product/product.html', {'products': products})


def customers(request):
    customers = Customer.objects.all()

    return render(request, 'product/customer.html', {'customers': customers})


def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders': orders
    }

    return render(request, 'product/customer-details.html', context)


def customer_create(request):
    form = CustomerForm()

    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/customers')

    context = {'form': form}

    return render(request, 'product/customer-create.html', context)


def customer_edit(request, id):
    customer = Customer.objects.get(id=id)
    form = CustomerForm(instance=customer)

    # update the customer
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/dashboard/customers/'+str(customer.id))

    context = {'form': form}
    return render(request, 'product/customer-edit.html', context)


def customer_delete(request, id):
    customer = Customer.objects.get(id=id)

    if request.method == "POST":
        customer.delete()
        return redirect('/dashboard/customers')

    context = {'customer': customer}

    return render(request, 'product/customer-delete.html', context)


def orders(request):
    orders = Order.objects.all()

    return render(request, 'product/order.html', {'orders': orders})
