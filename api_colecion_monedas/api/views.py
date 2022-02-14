from .models import Collector, Coin
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect
# Create your views here.


#Get a collector and update coins collection(Add-Delete coins of colector's colection)
#request (pk_collector, pk_coin)
@api_view(['GET', 'PUT'])
def collector_api_view(request):
    collector = Collector.objects.filter(id=request.data['pk_collector']).first()
    if collector:
        if request.method=='GET':            
            collector_serializer = CollectorSerializer(collector)
            return Response(collector_serializer.data)    
        if request.method == 'PUT':
            coin = Coin.objects.filter(id=request.data['pk_coin']).first()
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
    return Response({'message':'The Collector does not exist'})

    
#returns all the coins of the collection and validates if the collector has each coin
#reques (pk_collector, pk_collection)
@api_view(['GET'])
def coins_collector_api_view(request):
    if request.method == 'GET':
        collector = Collector.objects.filter(id = request.data['pk_collector']).first()
        coins_collection = Coin.objects.filter(id_collection =request.data['pk_collection'])
        if collector and coins_collection:
            coins_collector_send = []
            coins_collector = collector.coins.all()
            for coin in coins_collection:
                coin_send = {
                    "coin_number":coin.coin_number,
                    "name":coin.name,
                    "year":coin.year,
                    "description":coin.description,
                    "found":False,
                    "image":image_serializer(coin.image),               
                }
                if coins_collector.filter(id = coin.id).first():
                    coin_send['found'] = True           
                coins_collector_send.append(coin_send)
            return Response(coins_collector_send)
        else:
            return Response({'message':'Error'})


#Creates a Collector (User)
#request(username, password, email, coins)
@api_view(['POST'])
def new_collector_api_view(request):
    if request.method == 'POST':
        collector_serializer = CollectorSerializer(data=request.data)
        if collector_serializer.is_valid():
            collector_serializer.save()    
            return Response(collector_serializer.data)
        return Response(collector_serializer.errors)


#Login, returns the id of a matching collector
#request (username, password)
@api_view(['GET'])
def login_collector_api_view(request):
    if request.method == 'GET':
        collector = Collector.objects.filter(username = request.data['username'], password = request.data['password']).first()
        if collector:
            colllector_sirializer = CollectorSerializer(collector)
            return Response(colllector_sirializer.data)
        else:
            return Response({'message':'invalid username or password'})