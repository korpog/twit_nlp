from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.list_tweets, name='results'),
]
