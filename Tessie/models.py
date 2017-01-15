from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    author= models.CharField(max_length=100) 
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category_id = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

