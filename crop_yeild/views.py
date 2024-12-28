from django.shortcuts import render
from .models import TemperatureHumidity
from .serializers import TempHumiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def temp_humi_list(request, format=None):

    if request.method == 'GET':
        tem_humis = TemperatureHumidity.objects.all()
        serializer =  TempHumiSerializer(tem_humis, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TempHumiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def temp_humi_detail(request,id, format=None):
    try:
        tem_humi = TemperatureHumidity.objects.get(pk=id)
    except TemperatureHumidity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TempHumiSerializer(tem_humi)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TempHumiSerializer(tem_humi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tem_humi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)