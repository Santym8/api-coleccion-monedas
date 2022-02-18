from django.urls import path
from .views import *
urlpatterns = [

    #Create collector(User)
    #request(username, password, email, <coins>)
    path('collector/new/', new_collector_api_view, name='new_collector'), 

    
    #Login collector
    #request (username, password)
    path('collector/login/', login_collector_api_view, name='login_collector'),



    #Add or delete a coin of the collector's collection
    #request (pk_collector, pk_coin)
    path('collector/', collector_api_view, name='collector'),   


    #Get all coins and validate if a collector has each coin
    #reques (pk_collector, pk_collection)
    path('collector/coins/', coins_collector_api_view, name='coins_collector'),


    #Get all collections
    path('collections', collection_api_view, name='collections'),





]
