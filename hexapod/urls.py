from django.contrib import admin
from django.urls import path,include
from hexapod import views

urlpatterns = [
    path('', views.home,name="home"),
    path('results', views.results,name="results"),
    path('profile', views.profile,name="profile"),
]