from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from ..models.boardExtraColumnModel import BoardExtraColumnModel
from ..serializers.boardExtraColumnSerializer import BoardExtraColumnSerializer

class BoardExtraColumnView(APIView):
    permission_classes = [permissions.AllowAny]
    
    ###############################################################################################
    # 전체 추가 컬럼 조회
    ###############################################################################################
    def get(self, request):
        queryset = BoardExtraColumnModel.objects.all()
        serializer = BoardExtraColumnSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    ###############################################################################################
    # 추가 컬럼 추가
    ###############################################################################################
    def post(self, request):
        
        serializer = BoardExtraColumnSerializer(data = request.data)
        
        if ( serializer.is_valid() ):
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    