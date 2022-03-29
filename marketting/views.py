from django.shortcuts import render
from matplotlib.font_manager import json_dump
from marketting.models import Note

# Create your views here.


def welcome(request):
    # get some data from database or an api

    # get all the notes and send it to welcome page
    notes = Note.objects.all()
    return json_dump(notes)

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
