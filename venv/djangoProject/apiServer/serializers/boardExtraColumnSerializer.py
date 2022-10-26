from pyexpat import model
from rest_framework import serializers
from .. models . boardExtraColumnModel import BoardExtraColumnModel

class BoardExtraColumnSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BoardExtraColumnModel
        fields = ['columnSeq','boardSeq','columnName','sort','createDate','modifyDate']
        