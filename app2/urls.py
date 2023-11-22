from app2.views import *
from django.urls import path
app_name= "everything"

urlpatterns =[

    path('sahi/',sahi,name='sahi'),
]