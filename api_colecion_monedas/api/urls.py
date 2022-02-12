from django.urls import path
from .views import *
urlpatterns = [
    path('collector/<int:pk>', collector_api_view, name='collector'),
    path('collector/<int:pk>/<int:pk_coin>', collector_api_view, name='collector'),
    path('collector/new/', new_collector_api_view, name='collector'),

]
