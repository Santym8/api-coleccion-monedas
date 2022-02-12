from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Collector
from django.contrib.auth.models import User

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'