from django.db import models

class BoardListModel(models.Model):
    boardSeq = models.AutoField(primary_key=True)
    boardName = models.CharField(max_length=200)
    sort = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)