from django.contrib.auth.models import User, Group
from core.models import Cadastro
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CadastroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cadastro
        fields = ('id', 'url', 'nome', 'data_nascimento', 'genero', 'escolaridade')
