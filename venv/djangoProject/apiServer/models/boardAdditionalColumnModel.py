from django.db import models
from . boardListModel import BoardListModel

class BoardAdditionalColumnModel(models.Model):
    columnSeq = models.AutoField(primary_key=True)
    boardSeq = models.ForeignKey(BoardListModel, on_delete=models.CASCADE, related_name='boardAdditionalColumn')
    columnName = models.CharField(max_length=200)
    sort = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)