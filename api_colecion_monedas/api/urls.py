from django.urls import path
from .views import *
urlpatterns = [
    path('collector/<int:pk>/', collector_api_view, name='collector'),
    path('collector/add_delete_coin/<int:pk>/<int:pk_coin>/', collector_api_view, name='collector'),
    path('collector/coins/<int:pk_collector>/<int:pk_collection>/', coins_collector_api_view, name='coins_collector'),
    path('collector/new/', new_collector_api_view, name='collector'),

]
