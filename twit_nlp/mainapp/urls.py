from django.urls import path
from . import views

urlpatterns = [
    path('results/', views.TwitterFormView.as_view(), name='sentiment'),
]
