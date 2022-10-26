from django.db import models
from . boardModel import BoardModel

class BoardExtraColumnModel(models.Model):
    columnSeq = models.AutoField(primary_key=True)
    boardSeq = models.ForeignKey(BoardModel, on_delete=models.CASCADE, related_name='boardExtraColumn')
    columnName = models.CharField(max_length=200)
    sort = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)