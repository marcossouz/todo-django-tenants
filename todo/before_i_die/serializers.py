from rest_framework import serializers

from .models import BeforeIDie


class BeforeIDieSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeforeIDie
        fields = ['text', 'checkbox']
