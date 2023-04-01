from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from webapi.models import Auto, AutoColor, Color
from webapi.serializers import AutoSerializer, AutoColorSerializer, ColorSerializer



from rest_framework.decorators import api_view
from django.db.utils import IntegrityError

from django.db.models import Count


from pymongo import MongoClient

from webapi.dbclasses.cliente import ClienteCollection
from django.db.models import Case, When, Value, IntegerField

import pandas as pd 

# Create your views here.
@api_view(['POST'])
def auto_list(request):
    if request.method == 'POST':
        auto_data = JSONParser().parse(request)
        auto_serializer = AutoSerializer(data=auto_data)
        if auto_serializer.is_valid():
            auto_serializer.save()
            return JsonResponse(auto_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(auto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def auto_detail(request, id):
    auto = get_object_or_404(auto, id=id)
    if request.method == 'GET':
        auto_serializer = AutoSerializer(auto)
        return JsonResponse(auto_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'PUT':
        auto_data = JSONParser().parse(request)
        auto_data["id"] = id
        auto_serializer = AutoSerializer(auto, data=auto_data)
        if auto_serializer.is_valid():
            auto_serializer.save()
            return JsonResponse(auto_serializer.data)
        return JsonResponse(auto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auto.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def auto_color(request, id):
    auto = get_object_or_404(auto, id=id)
    if request.method == 'GET':
        colores = AutoColor.objects.filter(id_auto=auto)
        color_serializer = AutoColorSerializer(colores, many=True)
        return JsonResponse(color_serializer.data, safe=False)
    
    elif request.method == 'POST':
        color_data = JSONParser().parse(request)
        color_data["id_auto"] = id
        color_serializer = AutoColorSerializer(data=color_data)
        if color_serializer.is_valid():
            color_serializer.save()
            return JsonResponse(color_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(color_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def auto_color_detail(request, id, id_color):
    if request.method == 'DELETE':
        auto = get_object_or_404(auto, id=id)
        color = get_object_or_404(Color, id=id_color)
        auto_color = get_object_or_404(AutoColor, id_color=color, id_auto=auto)        
        auto_color.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    