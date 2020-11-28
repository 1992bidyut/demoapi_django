from django.shortcuts import render
from django.http import  JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import SwitchBoxSerializer
from .models import SwitchBox
# Create your views here.
@api_view(['GET'])
def iotcoreOverview(request):
    res={
        "main-path":"/api/",
        "switch=list":"api/switch-list/",
        "switchdetails":"api/switch-detail/{index}/",
        "switch-create":"api/switch-create",
        "switch-update": "/api/switch-update/{index}/",
        "switch-delete": "api/switch-create"
    }
    return Response(res)

@api_view(['GET'])
def switchList(request):
    switchs=SwitchBox.objects.all()
    serializer = SwitchBoxSerializer(switchs,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def switchDetail(request,pk):
    switchs=SwitchBox.objects.get(id=pk)
    serializer = SwitchBoxSerializer(switchs,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def switchCreate(request):
    serializer = SwitchBoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def switchUpdate(request,pk):
    switchs = SwitchBox.objects.get(id=pk)
    serializer = SwitchBoxSerializer(instance=switchs,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def switchDelete(request,pk):
    switchs = SwitchBox.objects.get(id=pk)
    switchs.delete()
    return Response("Item deleted!")