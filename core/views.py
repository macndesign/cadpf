from django.contrib.auth.models import User, Group
from core.models import Cadastro
from rest_framework import viewsets
from core.serializers import UserSerializer, GroupSerializer, CadastroSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CadastroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cadastros to be viewed or edited.
    """
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer