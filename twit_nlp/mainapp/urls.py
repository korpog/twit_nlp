from django.urls import path
from . import views

urlpatterns = [
    path('sentiment/', views.analyse_tweets, name='sentiment'),
]
