from . import views
from MyApp import api
from django.urls import path

urlpatterns = [
 path('', views.dht11, name='data'),
 path('api/list', api.Dlist, name='DHT11List'),
 path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
 path('data2/', views.dht112, name='data2'),
 path('data3/', views.dht113, name='data3'),
 path('jour1/', views.jour1, name='jour1'),
 path('jour2/', views.jour1, name='jour2'),
 path('jour3/', views.jour1, name='jour3'),
 path('Gjour1/', views.Gjour1, name='Gjour1'),
 path('Gjour2/', views.Gjour2, name='Gjour2'),
 path('Gjour3/', views.Gjour3, name='Gjour3'),
 path('historique/', views.historique, name='historique'),
 path('hist/', views.hist, name='hist'),
]

