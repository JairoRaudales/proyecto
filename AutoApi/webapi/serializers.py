from rest_framework import serializers 
from webapi.models import Auto,TipoAuto,Color,Marca,Modelo,Estado,AutoColor,Cliente,Genero

class TipoAutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoAuto
        fields = ('id', 'descripcion')

class AutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auto
        fields = ('id', 'id_tipo_carro', 'id_marca', 'id_modelo', 'id_estado', 'precio', 'año', 'observaciones')

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'descripcion')

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'descripcion', 'id_tipo_auto')

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id', 'descripcion')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('id', 'descripcion')

class AutoColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoColor
        fields = ('id', 'id_color', 'id_auto')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('id', 'descripcion')

class ClienteSerializer(serializers.ModelSerializer):

    def validate_id(self, value):
        if Cliente.objects.filter(id=value).exists():
            raise serializers.ValidationError('Ya esta registrado un cliente con este id')
        return value
    
    class Meta:
        model = Cliente
        fields = ('id_nacional', 'nombre', 'apellido', 'telefono', 'direccion', 'genero', 'fecha_nacimiento', 'email')