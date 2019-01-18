from django.urls import path
from . import views

urlpatterns = [
    path('sentiment/', views.get_twitter_sentiment, name='sentiment'),
    path('statistics/', views.get_stats, name='statistics'),
]
