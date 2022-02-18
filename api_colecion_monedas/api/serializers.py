from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Collection, Collector
import base64

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = ['id','username', 'email']

class NewCollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'


