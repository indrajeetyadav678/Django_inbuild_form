from rest_framework import serializers
from .models import*

class registserializer(serializers.ModelSerializer):
    class Meta:
        model=RegistrationModel
        fields='__all__'