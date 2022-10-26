from django.db import models
from . boardExtraColumnModel import BoardExtraColumnModel
from . postDataModel import PostDataModel

class PostExtraDataModel(models.Model):
    postExtraSeq = models.AutoField(primary_key=True)
    postSeq = models.ForeignKey(PostDataModel, on_delete=models.CASCADE, related_name='postExtraData')
    columnSeq = models.ForeignKey(BoardExtraColumnModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    createDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)