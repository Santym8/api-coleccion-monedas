from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import Collector
import base64

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'

class CollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = ['id','username', 'email']

class NewCollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collector
        fields = '__all__'


def image_serializer(url_image):
    with open(url_image, mode='rb') as file:
        img = file.read()
    return base64.encodebytes(img).decode('utf-8')
