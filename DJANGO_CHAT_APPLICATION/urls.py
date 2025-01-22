from django.urls import path
from . import views

urlpatterns = [
       path('', views.chat_list, name='chat_list'),
       path('chat/<str:username>/', views.chat_room, name='chat_room'),
   ]