from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home' ),
    path('inputODE/', views.inputODE, name='inputODE' ),
    path('submitODE/<int:num>/', views.submitODE, name='submitODE' ),
    path('documentation/', views.documentation, name='documentation' ),
    path('about/', views.about, name='about' ),
]