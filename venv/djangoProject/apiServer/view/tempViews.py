from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from .. models import Temp
from .. serializers import TempSerializer

# http method 정의
@api_view(['GET'])
def tempJson(request):
  queryset = Temp.objects.all() # 모델 데이터
  serializer = TempSerializer(queryset, many=True) # serializer
  print("-----------------------------")
  print(queryset)
  print(serializer)
  print(serializer.data)
  print(JSONRenderer().render(serializer.data))
  print("-----------------------------")
  return Response(serializer.data)
