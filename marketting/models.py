from pydoc import describe
from django.db import models

# Create your models here.
class Note(models.Model):
    name = models.CharField(max_length=20)
    decription = models.TextField()

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    comment = models.CharField(max_length=200, null=True)