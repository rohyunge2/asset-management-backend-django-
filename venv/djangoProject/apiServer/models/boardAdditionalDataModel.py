from django.db import models
from . boardAdditionalColumnModel import BoardAdditionalColumnModel
from . boardCommonDataModel import BoardCommonDataModel

class BoardAdditionalDataModel(models.Model):
    boardAddDataSeq = models.AutoField(primary_key=True)
    boardDataSeq = models.ForeignKey(BoardCommonDataModel, on_delete=models.CASCADE, related_name='boardAdditionalData')
    columnSeq = models.ForeignKey(BoardAdditionalColumnModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    createDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)