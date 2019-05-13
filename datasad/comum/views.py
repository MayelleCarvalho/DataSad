from django.shortcuts import render
from datasad.comum.models import Perfil
from datasad.comum.serializers import PerfilSerializer
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_condition import Or
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope, OAuth2Authentication
from rest_framework.authentication import SessionAuthentication
class PerfilList(generics.ListCreateAPIView):

    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    authentication_classes = [OAuth2Authentication, SessionAuthentication]
    permission_classes = [Or(IsAdminUser, TokenHasReadWriteScope)]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = '__all__'