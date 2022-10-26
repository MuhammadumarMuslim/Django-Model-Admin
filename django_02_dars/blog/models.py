from operator import mod
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    age = models.SmallIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} "

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"