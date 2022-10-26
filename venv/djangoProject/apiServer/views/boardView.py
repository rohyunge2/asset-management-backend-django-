from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .. models . boardModel import BoardModel
from .. serializers . boardSerializer import BoardSerializer

class BoardView(APIView):
    permission_classes = [permissions.AllowAny]
    
    ###############################################################################################
    # 전체 게시판 조회
    ###############################################################################################
    def get(self, request):
        queryset = BoardModel.objects.all()
        serializer = BoardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    ###############################################################################################
    # 게시판 추가
    ###############################################################################################
    def post(self, request):
        
        serializer = BoardSerializer(data = request.data)
        
        if ( serializer.is_valid() ):
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    