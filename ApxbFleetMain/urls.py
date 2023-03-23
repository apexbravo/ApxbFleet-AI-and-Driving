from django.urls import path
from . import views


app_name = 'ApxbFleetMain'

urlpatterns = [
    path('', views.index, name='index'),
]
