from django.urls import path
from . import views


app_name = 'ApxbFleetMain'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('drivers_list/', views.driver_list, name='drivers_list'),
    path('create_driver/', views.create_driver, name='create_driver')
]
