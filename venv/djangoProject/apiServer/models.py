from msilib import sequence
from turtle import title
from django.db import models

class Temp(models.Model):
    sequence = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    createUser = models.CharField(max_length=200)