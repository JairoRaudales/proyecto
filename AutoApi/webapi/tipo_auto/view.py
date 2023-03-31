from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.parsers import JSONParser
from rest_framework import status

from webapi.models import TipoAuto, Marca
from webapi.serializers import TipoAutoSerializer, MarcaSerializer
from rest_framework.decorators import api_view

from django.db.models import Count
# Create your views here.

@api_view(['GET', 'POST'])
def tipo_auto_list(request):
    if request.method == 'GET':
        tipo_auto = TipoAuto.objects.all()
        tipo_auto_serializer = TipoAutoSerializer(tipo_auto, many=True)
        return JsonResponse(tipo_auto_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tipo_auto_data = JSONParser().parse(request)
        tipo_auto_serializer = TipoAutoSerializer(data=tipo_auto_data)
        if tipo_auto_serializer.is_valid():
            tipo_auto_serializer.save()
            return JsonResponse(tipo_auto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(tipo_auto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def tipo_auto_marcas_list(request, id):
    tipo_auto = get_object_or_404(TipoAuto, id=id)
    if request.method == 'GET':
        marca = Marca.objects.filter(id_tipo_auto=tipo_auto)
        marca_serializer = MarcaSerializer(marca, many=True)
        return JsonResponse(marca_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        payload = request.data
        
        marca_data = {'descripcion': payload['descripcion'], 'id_tipo_auto': tipo_auto.id}
        marca_serializer = MarcaSerializer(data=marca_data)
        
        if marca_serializer.is_valid():
            marca_serializer.save()
            return JsonResponse(marca_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(marca_serializer.errors, status=status.HTTP_400_BAD_REQUEST)