from django.db import models

# Create your models here.
class Rifle(models.Model):
    name = models.CharField(max_length=20, blank=False)
    place_of_origin = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name
    
class User(models.Model):
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.email