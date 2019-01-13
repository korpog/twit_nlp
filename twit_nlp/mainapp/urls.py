from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tweets, name='main'),
    path('results/', views.list_tweets, name='results'),
]
