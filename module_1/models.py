from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.email


class Rifle(models.Model):
    name = models.CharField(max_length=20, blank=False)
    place_of_origin = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name