from pyexpat import model
from rest_framework import serializers
from . models import Temp

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp
        fields = ('sequence', 'title', 'contents', 'createDate', 'createUser')