#aci9bw added this file

from django.urls import path
from . import views 

app_name= "oauth_app"
urlpatterns= [
    path('add_points/', views.add_points, name='add_points'), 
]
