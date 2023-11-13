from django.contrib.auth.models import Permission
from django.shortcuts import render
from .models import Developer
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .serializers import DeveloperModelSerializer


class DeveloperModelViewSet(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperModelSerializer