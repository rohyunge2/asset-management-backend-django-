from pyexpat import model
from rest_framework import serializers
from .. models . boardListModel import BoardListModel
from . boardAdditionalColumnSerializer import BoardAdditionalColumnSerializer

class BoardListSerializer(serializers.ModelSerializer):
    
    boardAdditionalColumn = BoardAdditionalColumnSerializer(many=True)
    
    class Meta:
        model = BoardListModel
        fields = ['boardSeq', 'boardName', 'sort', 'createDate', 'modifyDate', 'boardAdditionalColumn']