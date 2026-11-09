from rest_framework import serializers
from .models import IPR


class IPRSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPR
        fields = '__all__'