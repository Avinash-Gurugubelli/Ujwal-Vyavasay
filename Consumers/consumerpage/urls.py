from django.urls import path
from . import views

urlpatterns = [
    path('', views.consumerfunction),
    path('buy/', views.buy),
]