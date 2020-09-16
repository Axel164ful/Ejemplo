from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
app_name='peticion'
urlpatterns=[
	path('', views.pedir, name='pedir'),
	path('pedir2', views.pedir2, name= 'pedir2'),
	path('pedir3', views.pedir3, name='pedir3'),
]