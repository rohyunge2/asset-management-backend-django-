import imp
from pyexpat import model
from rest_framework import serializers
from .. models . boardCommonDataModel import BoardCommonDataModel
from . boardListSerializer import BoardListSerializer
from . boardAdditionalDataSerializer import BoardAdditionalDataSerializer

class BoardCommonDataSerializer(serializers.ModelSerializer):
    
    # def validate(self, data):
    #     if data['first_name'] == data['last_name']:
    #         raise serializers.ValidationError("first_name and last_name shouldn't be same.")
    #     return data
    
    boardAdditionalData = BoardAdditionalDataSerializer(many=True, read_only=True)
    
    class Meta:
        model = BoardCommonDataModel
        fields = ['boardDataSeq','boardSeq','modelName','serialNum','userName','deptName','checkOutDate','checkInDate','referNote','createDate','modifyDate', 'boardAdditionalData']
        
    # 읽기 시, 직렬화 지원 메소드
    def to_representation(self, instance):
        response = super().to_representation(instance)
        if isinstance(instance, dict):
            pass
        elif isinstance(instance, BoardCommonDataModel):
            response['boardData'] = BoardListSerializer(instance.boardSeq).data
            
        return response
    
    # 쓰기 시, 역직렬화 지원 메소드
    # https://www.django-rest-framework.org/api-guide/serializers/
    # BaseSerializer 참고
    
    # def to_internal_value():