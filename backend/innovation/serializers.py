from rest_framework import serializers
from .models import Innovation


class InnovationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Innovation
        fields = '__all__'