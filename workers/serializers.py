from rest_framework.serializers import ModelSerializer
from .models import Worker
from django.contrib.auth.models import Permission
class WorkerModelSerializer(ModelSerializer):
    class Meta:
        model = Worker
        #lookup_field = 'username'
        fields = '__all__'



# class PermissionSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Permission