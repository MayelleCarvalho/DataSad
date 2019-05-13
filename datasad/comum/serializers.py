from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        # fields = ['id', 'sexo', 'contato', 'data_nascimento', 'usuario', 'cpf']
        fields = '__all__'