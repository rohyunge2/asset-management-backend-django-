from pyexpat import model
from rest_framework import serializers
from ..models.boardAdditionalDataModel import BoardAdditionalDataModel

class BoardAdditionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardAdditionalDataModel
        fields = '__all__'