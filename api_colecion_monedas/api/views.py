from .models import Collector
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
# Create your views here.


@api_view(['GET', 'PUT'])
def collector_api_view(request, pk=None, pk_coin=None):
    collector = Collector.objects.filter(id=pk).first()
    if collector:
        if request.method=='GET':            
            collector_serializer = CollectorSerializer(collector)
            return Response(collector_serializer.data)    
        if request.method == 'PUT':
            coins = collector._meta.get_field('coins')


    return Response({'message':'Error'})

@api_view(['POST'])
def new_collector_api_view(request):
    if request.method == 'POST':
        collector_serializer = CollectorSerializer(data=request.data)
        if collector_serializer.is_valid():
            collector_serializer.save()    
            return Response(collector_serializer.data)
        return Response(collector_serializer.errors)
        