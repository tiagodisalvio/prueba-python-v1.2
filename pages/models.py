from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#Modelo para crear un Post
class Post(models.Model):
    img = models.ImageField(upload_to='images', null=True, blank=True)
    place = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    def __str__(self):
        return f'{self.place} post by {self.name}'