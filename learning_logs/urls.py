'''Defining urls patterns for learning_logs'''

from django.urls import path
from . import views



app_name='learning_logs'
urlpatterns=[
    # Home page
    path('',views.index,name='index'),
    #page that shows all topics
   
    #Detail page for a single topic
    
]