from django.shortcuts import render
from matplotlib.font_manager import json_dump
from marketting.models import Note

# Create your views here.


def welcome(request):
    # get some data from database or an api

    # get all the notes and send it to welcome page
    notes = Note.objects.all()

    return render(request, 'welcome.html', context={
        "notes": list(notes),
        "name": "My todo list"
    })


def about_us(request):
    return render(request, 'about-us.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def year(request, year=2022):
    return render(request, 'year.html', {
        "year": year
    })

def update(request, id):

    # update a note
    note = Note.objects.get(id=id)
    note.name = "Updated Title"
    note.save()

    notes = Note.objects.all()

    return render(request, 'welcome.html', context={
        "notes": list(notes),
        "name": "My todo list"
    })

def delete(request, id):

    # delete a note
    note = Note.objects.get(id=id)
    note.delete()

    notes = Note.objects.all()

    return render(request, 'welcome.html', context={
        "notes": list(notes),
        "name": "My todo list"
    })

def create(request):

    # create a note
    note = Note(name="A name", decription="some text here")
    note.save()

    notes = Note.objects.all()

    return render(request, 'welcome.html', context={
        "notes": list(notes),
        "name": "My todo list"
    })
