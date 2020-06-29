from django.urls import path
from . import views

urlpatterns = [
    path('', views.hi, name='home-page'),
    path('getCountry/', views.get_country, name='getCountry'),
]