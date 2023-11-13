from rest_framework.serializers import ModelSerializer
from .models import Developer
from django.contrib.auth.models import Permission
class DeveloperModelSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'



