import imp
from pyexpat import model
from rest_framework import serializers
from .. models . boardCommonDataModel import BoardCommonDataModel
from . boardListSerializer import BoardListSerializer
from . boardAdditionalDataSerializer import BoardAdditionalDataSerializer

class BoardCommonDataSerializer(serializers.ModelSerializer):
    
    boardAdditionalData = BoardAdditionalDataSerializer(many=True)
    
    class Meta:
        model = BoardCommonDataModel
        fields = ['boardDataSeq','boardSeq','modelName','serialNum','userName','deptName','checkOutDate','checkInDate','referNote','createDate','modifyDate', 'boardAdditionalData']
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['boardData'] = BoardListSerializer(instance.boardSeq).data
        return response
        
    