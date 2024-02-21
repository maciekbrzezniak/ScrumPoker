from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_room/', views.create_room, name='create_room'),
    path('join_room/', views.join_room, name='join_room'),
    path('join_room/<uuid:room_id>/', views.join_room_detail, name='join_room_detail'),
    path('room/<uuid:room_id>/', views.room, name='room'),
    path('room/<uuid:room_id>/join/', views.join_room, name='join_room'),
]