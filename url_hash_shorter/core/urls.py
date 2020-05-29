# -*- coding: utf-8 -*-
from django.urls import path

from core import views
from core.apps import CoreConfig


app_name = CoreConfig.name

urlpatterns = [
    path('api/create_url/', views.create_url, name='create_url'),
    path('api/remove_url/<int:url_pk>', views.remove_url, name='remove_url'),
    path('links/', views.links, name='links'),
    path('<slug:slug>/', views.url_redirect, name='url_redirect'),
    path('', views.index, name='index'),
]
