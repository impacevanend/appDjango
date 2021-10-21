from django.db import models

# Create your models here.

class Blogger(models.Model):
    title = models.CharField(max_length= 200)
    body = models.TextField(max_length= 500)