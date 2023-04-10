from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ApxbFleetMain'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('drivers_list/', views.driver_list, name='drivers_list'),
    path('driver_detail/<int:pk>/', views.driver_detail, name='driver_detail'),
    path('create_driver/', views.create_driver, name='create_driver'),
    path('driver_edit/<int:pk>', views.driver_edit, name="driver_edit")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
