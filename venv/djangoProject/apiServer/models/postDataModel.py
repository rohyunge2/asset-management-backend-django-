from django.db import models
from . boardModel import BoardModel

class PostDataModel(models.Model):
    boardDataSeq = models.AutoField(primary_key=True)
    boardSeq = models.ForeignKey(BoardModel, on_delete=models.CASCADE)
    modelName = models.CharField(max_length=200)
    serialNum = models.CharField(max_length=200)
    userName = models.CharField(max_length=100)
    deptName = models.CharField(max_length=100)
    checkOutDate = models.DateTimeField(null=True, blank=True)
    checkInDate = models.DateTimeField(null=True, blank=True)
    referNote = models.TextField(null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)
    
    