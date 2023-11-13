from django.contrib.auth.models import Permission
from django.shortcuts import render
from .models import Worker
from rest_framework.viewsets import ModelViewSet
from rest_framework.renderers import JSONRenderer
from .serializers import WorkerModelSerializer

# class PermissionViewSet(ModelViewSet):
#     """
#     API endpoint that allows permissions to be viewed or edited.
#     """
#     queryset = Permission.objects.all()
#     serializer_class =  PermissionSerializer

class WorkerModelViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerModelSerializer
