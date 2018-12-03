from rest_framework import serializers
from .models import Persona, Articulo


class PersonaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Persona
        fields = ('nombre', 'correo', 'contrasenia' , 'foto')
 
class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Articulo
        fields = ('nameD', 'cantidad', 'desc', 'fotoD')