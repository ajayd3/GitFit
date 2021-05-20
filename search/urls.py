from django.urls import path
from . import views 

app_name= "search"
urlpatterns= [
    path('', views.index, name= 'index'),
    path('watch_video/', views.watch_video, name='watch_video'), 
]