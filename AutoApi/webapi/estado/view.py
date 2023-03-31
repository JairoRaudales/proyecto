from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from webapi.models import Estado
from webapi.serializers import EstadoSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def estado_list(request):
    if request.method == 'GET':
        estado = Estado.objects.all()
        estado_serializer = EstadoSerializer(estado, many=True)
        return JsonResponse(estado_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        estado_data = JSONParser().parse(request)
        estado_serializer = EstadoSerializer(data=estado_data)
        if estado_serializer.is_valid():
            estado_serializer.save()
            return JsonResponse(estado_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(estado_serializer.errors, status=status.HTTP_400_BAD_REQUEST)