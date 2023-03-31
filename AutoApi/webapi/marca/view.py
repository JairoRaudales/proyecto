from django.shortcuts import render

# Create your views here.
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework import status

from webapi.models import Marca
from webapi.serializers import MarcaSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def marca_list(request):
    if request.method == 'GET':
        marca = marca.objects.all()
        marca_serializer = MarcaSerializer(marca, many=True)
        return JsonResponse(marca_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        marca_data = JSONParser().parse(request)
        marca_serializer = MarcaSerializer(data=marca_data)
        if marca_serializer.is_valid():
            marca_serializer.save()
            return JsonResponse(marca_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(marca_serializer.errors, status=status.HTTP_400_BAD_REQUEST)