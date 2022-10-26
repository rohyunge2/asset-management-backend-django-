from pyexpat import model
from rest_framework import serializers
from .. models . boardModel import BoardModel
from . boardExtraColumnSerializer import BoardExtraColumnSerializer

class BoardSerializer(serializers.ModelSerializer):
    
    boardAdditionalColumn = BoardExtraColumnSerializer(many=True, read_only=True)
    
    class Meta:
        model = BoardModel
        fields = ['boardSeq', 'boardName', 'sort', 'createDate', 'modifyDate', 'boardAdditionalColumn']