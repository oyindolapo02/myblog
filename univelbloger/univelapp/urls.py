from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('article/', views.article, name='article'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
]