from django.db import models

# Create your models here.

#created first model Url
class Url(models.Model):
    link = models.CharField(max_length=10000)
    uuid = models.CharField(max_length=10)