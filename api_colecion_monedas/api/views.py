from .models import Collector, Coin
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
# Create your views here.


#Get a collector and update coins collection(Add-Delete coins of colector's colection)
@api_view(['GET', 'PUT'])
def collector_api_view(request, pk=None, pk_coin=None):
    collector = Collector.objects.filter(id=pk).first()
    if collector:
        if request.method=='GET':            
            collector_serializer = CollectorSerializer(collector)
            return Response(collector_serializer.data)    
        if request.method == 'PUT':
            coin = Coin.objects.filter(id=pk_coin).first()
            if coin:
                coins_collector = collector.coins.filter(id=coin.id).first()
                if coins_collector:               
                    collector.coins.remove(coin.id) 
                else:
                    collector.coins.add(coin.id)             
                collector.save()
                collector_serializer = CollectorSerializer(collector)
                return Response(collector_serializer.data)
            else: 
                return Response({'message':"The Coin does not exist"})            
    return Response({'message':'Error'})


def image_serializer(url_image):
    #To-do ImageSerializer
    return url_image
    
#returns all the coins of the collection and validates if the collector has each coin
@api_view(['GET'])
def coins_collector_api_view(request, pk_collector=None, pk_collection = None):
    if request.method == 'GET':
        collector = Collector.objects.filter(id = pk_collector).first()
        coins_collection = Coin.objects.filter(id_collection = pk_collection)
        if collector and coins_collection:
            coins_collector_send = []
            coins_collector = collector.coins.all()
            for coin in coins_collection:
                coin_send = {
                    "coin_number":coin.coin_number,
                    "name":coin.name,
                    "year":coin.year,
                    "description":coin.description,
                    "image":image_serializer(coin.image),
                    "found":False
                }
                if coins_collector.filter(id = coin.id).first():
                    coin_send['found'] = True           
                coins_collector_send.append(coin_send)
            return Response(coins_collector_send)
        else:
            return Response({'message':'Error'})


#Create a Collector (User)
@api_view(['POST'])
def new_collector_api_view(request):
    if request.method == 'POST':
        collector_serializer = CollectorSerializer(data=request.data)
        if collector_serializer.is_valid():
            collector_serializer.save()    
            return Response(collector_serializer.data)
        return Response(collector_serializer.errors)
        