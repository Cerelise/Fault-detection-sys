import requests
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action,api_view
from rest_framework.views import APIView
from django.http import HttpResponse

from .serializer import TrainsSerializer,MultipleTrainsSerializer,TestsSerializer
from .models import TrainsUpload,TestsUpload

BASE_URL = 'http://127.0.0.1:8000'

class TrainsViewSet(ModelViewSet):
    queryset = TrainsUpload.objects.all()  
    serializer_class = TrainsSerializer

    @action(detail=False,methods=['POST'])
    def multiple_upload(self,request,*args,**kwargs):
        serializer = MultipleTrainsSerializer(data=request.data or None)
        serializer.is_valid(raise_exception=True)
        trains = serializer.validated_data.get("trains")
        trains_list = []
        for train in trains:
            trains_list.append(TrainsUpload(train=train))

        if trains_list:
            TrainsUpload.objects.bulk_create(trains_list)
        
        return Response("ok")

class TestsViewSet(ModelViewSet):
    queryset = TestsUpload.objects.all()  
    serializer_class = TestsSerializer


class HandleResult(APIView):
    # 转换为[{id:1,res:4},{id:2,res:2}...] 的数据
    def get(self, request):
        url = BASE_URL + '/upload/res/result_pred.json'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            result = [{'id': i + 1, 'res_type': item[1]} for i, item in enumerate(data)]
            return Response(result)
        else:
            return Response(status=response.status_code)



def load_model(request):
    model_path = BASE_URL + '/upload/res/rf.pkl'
    response = requests.get(model_path)
    if response.status_code == 200:
        file_content = response.content
        response = HttpResponse(file_content, content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="user_rf.pkl"'
        return response
    else:
        return Response("Failed")

