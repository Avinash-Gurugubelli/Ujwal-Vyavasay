from django.urls import path

from . import views

urlpatterns = [
    path('',views.c_account)
]