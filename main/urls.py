from django.contrib import admin
from django.urls import path, include
from .views import group_list, create_group,messages, send_message, register_view, login_view, logout_view

urlpatterns = [
    path('', group_list, name='group_list'),
    path('create_group', create_group, name='create_group'),
    path('messages/<str:slug>', messages, name='messages'),
    path('send_message/<str:slug>', send_message, name='send_message'),
    path('register', register_view, name="register"),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout')
]
