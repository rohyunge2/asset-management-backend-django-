from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .. models . boardCommonDataModel import BoardCommonDataModel
from .. serializers . boardCommonDataSerializer import BoardCommonDataSerializer

class BoardCommonDataDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    
    ###############################################################################################
    # 단일 게시글 조회
    ###############################################################################################
    def get(self, request, seq):
        queryset = BoardCommonDataModel.objects.get(boardDataSeq = seq)
        serializer = BoardCommonDataSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    ###############################################################################################
    # 단일 게시글 수정
    ###############################################################################################
    def put(self, request, seq):
        
        queryset = BoardCommonDataModel.objects.get(boardDataSeq = seq)
        serializer = BoardCommonDataSerializer(queryset, data = request.data)
        
        if ( serializer.is_valid() ):
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    ###############################################################################################
    # 단일 게시글 삭제
    ###############################################################################################
    def delete(self, request, seq):
        
        queryset = BoardCommonDataModel.objects.get(boardDataSeq = seq)
        queryset.delete()
        
        return Response(status=status.HTTP_200_OK)