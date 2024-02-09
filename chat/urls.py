from django.urls import path 
from . import views 


app_name = 'chat'
urlpatterns = [
    path('',views.home,name='home'),
    path('room/<str:id>/',views.room,name='room')
]