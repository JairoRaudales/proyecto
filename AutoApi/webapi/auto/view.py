from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from webapi.models import auto, AutoColores, Color, AutoObservacion, Observacion
from webapi.serializers import AutoSerializer, AutoColoresSerializer, ColorSerializer, AutoObservacionSerializer, ObservacionSerializer

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
def auto_colores(request, id):
    auto = get_object_or_404(auto, id=id)
    if request.method == 'GET':
        colores = AutoColores.objects.filter(id_auto=auto)
        colores_serializer = AutoColoresSerializer(colores, many=True)
        return JsonResponse(colores_serializer.data, safe=False)
    
    elif request.method == 'POST':
        colores_data = JSONParser().parse(request)
        colores_data["id_auto"] = id
        colores_serializer = AutoColoresSerializer(data=colores_data)
        if colores_serializer.is_valid():
            colores_serializer.save()
            return JsonResponse(colores_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(colores_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def auto_colores_detail(request, id, id_color):
    if request.method == 'DELETE':
        auto = get_object_or_404(auto, id=id)
        color = get_object_or_404(Color, id=id_color)
        auto_color = get_object_or_404(AutoColores, id_color=color, id_auto=auto)        
        auto_color.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST', 'GET'])
def auto_observacion(request, id):
    
    
    auto = get_object_or_404(Auto, id=id)    
    
    if request.method == 'POST':
        observacion_data = JSONParser().parse(request)
        observacion_data["id_auto"] = id
        
        observacion_id = observacion_data["id_observacion"]
        observacion = Observacion.objects.get(id=observacion_id)

        auto_observacion = AutoObservacion.objects.filter(id_auto=auto, id_observacion=observacion)
        if len(auto_observacion) > 0:
            return JsonResponse({"error": "Observacion ya existe"}, status=status.HTTP_400_BAD_REQUEST)

        observacion_serializer = AutoObservacionSerializer(data=observacion_data)
        if observacion_serializer.is_valid():
            observacion_serializer.save()
            return JsonResponse(observacion_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(observacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        
        observaciones = Observacion.objects.all().values()
        
        auto_observaciones = AutoObservacion.objects.filter(
            id_auto=auto
        ).values(
            'id_auto'
            ,'descripcion'
            ,'id_observacion'
        ).distinct()        

        
        df_observaciones = pd.DataFrame(list(observaciones))        
        df_auto_observaciones = pd.DataFrame(list(auto_observaciones), columns=['id_auto','descripcion','id_observacion'])
        
        df_observaciones.columns = ['id','observacion']
        df_result = df_observaciones.merge(df_auto_observaciones, how='left', left_on='id', right_on='id_observacion')
        
        df_result['has_observacion'] = False
        df_result.loc[df_result['id_auto'].notnull(), 'has_observacion'] = True
        
        df_result = df_result.loc[:, ['id','observacion','descripcion','has_observacion']]



        #retornamos df_observaciones
        return JsonResponse(list(df_result.to_dict('records')), safe=False)
        
    
@api_view(['DELETE'])
def auto_observacion_detail(request, id, id_observacion):
    if request.method == 'DELETE':
        auto = get_object_or_404(Auto, id=id)
        observacion = get_object_or_404(Observacion, id=id_observacion)
        auto_observacion = get_object_or_404(AutoObservacion, id_observacion=observacion, id_auto=auto)        
        auto_observacion.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    