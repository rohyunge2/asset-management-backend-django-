from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from .. models . postDataModel import PostDataModel
from .. serializers . postDataSerializer import PostDataSerializer

class PostDataView(APIView):
    permission_classes = [permissions.AllowAny]
    
    ###############################################################################################
    # 전체 게시글 조회
    ###############################################################################################
    def get(self, request):
        queryset = PostDataModel.objects.all()
        serializer = PostDataSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    ###############################################################################################
    # 게시글 작성
    ###############################################################################################
    def post(self, request):
        
        serializer = PostDataSerializer(data = request.data)
        
        if ( serializer.is_valid() ):
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    