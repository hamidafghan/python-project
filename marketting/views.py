from django.shortcuts import render

# Create your views here.


def welcome(request):
    # get some data from database or an api
    return render(request, 'welcome.html', {
        "name": "My todo list application"
    })


def about_us(request):
    return render(request, 'about-us.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def year(request, year=2022):
    return render(request, 'year.html', {
        "year": year
    })
