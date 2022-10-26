from pyexpat import model
from rest_framework import serializers
from .. models . postExtraDataModel import PostExtraDataModel

class PostExtraDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostExtraDataModel
        fields = '__all__'