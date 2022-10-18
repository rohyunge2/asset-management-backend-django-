from pyexpat import model
from rest_framework import serializers
from .. models . boardAdditionalColumnModel import BoardAdditionalColumnModel

class BoardAdditionalColumnSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BoardAdditionalColumnModel
        fields = ['columnSeq','boardSeq','columnName','sort','createDate','modifyDate']
        