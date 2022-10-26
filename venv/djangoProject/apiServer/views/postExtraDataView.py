from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from ..models.postExtraDataModel import PostExtraDataModel
from ..serializers.postExtraDataSerializer import PostExtraDataSerializer

class PostExtraDataView(APIView):
    permission_classes = [permissions.AllowAny]
    
    ###############################################################################################
    # 전체 추가 컬럼 데이터 조회
    ###############################################################################################
    def get(self, request):
        queryset = PostExtraDataModel.objects.all()
        serializer = PostExtraDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    ###############################################################################################
    # 추가 컬럼 데이터 추가
    ###############################################################################################
    def post(self, request):
        
        serializer = PostExtraDataSerializer(data = request.data)
        
        if ( serializer.is_valid() ):
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    