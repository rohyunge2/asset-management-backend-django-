from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer

from .. models . boardListModel import BoardListModel
from .. models . boardCommonDataModel import BoardCommonDataModel
from .. serializers . boardListSerializer import BoardListSerializer
from .. serializers . boardCommonDataSerializer import BoardCommonDataSerializer

class BoardCommonDataView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        queryset = BoardCommonDataModel.objects.all()
        serializer = BoardCommonDataSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("----------------------------------------------------")
        print("----------------------------------------------------")
        print(request.data)
        print(request.data.get("123"))
        
        BoardCommonDataModel.save()
        
        return Response("POST 테스트")
    
    def put(self, request):
        return Response("PUT 테스트")
    
    def delete(self, request):
        return Response("DELETE 테스트")
    