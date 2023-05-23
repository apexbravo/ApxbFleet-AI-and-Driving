from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from ApxbFleetMain.context_processors import language_info_list
from .models import Driver, DriverLocation, DriverBehavior
from .forms import DriverForm
from django.db.models import Count
# Create your views here.
from celery import Celery
from celery.schedules import crontab
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.utils.translation import activate
from django.utils.translation import get_language_info
from django.utils.translation import gettext

app = Celery('ApxbFleetMain', broker='redis://localhost:6379/0')

app.conf.beat_schedule = {
    'update-driver-location': {
        'task': 'ApxbFleetMain.tasks.schedule_update_driver_location',
        'schedule': crontab(minute='*/1'),  # run every 15 minutes
    },
}


def index(request) -> HttpResponse:
    languages = language_info_list(request)
    return render(request, 'ApxbFleetMain/index.html', {'languages': languages})


def login(request) -> HttpResponse:
    return render(request, 'ApxbFleetMain/login.html')


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'ApxbFleetMain/pages/drivers/index.html', {'drivers': drivers})


def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    driver_location = DriverLocation.objects.filter(
        driver=driver).order_by('timestamp').first()
    return render(request, 'ApxbFleetMain/pages/drivers/details.html', {'driver': driver, 'driver_location': driver_location})


def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.save()
            return redirect('ApxbFleetMain:drivers_list')
    else:
        form = DriverForm()
    return render(request, 'ApxbFleetMain/pages/drivers/add.html', {'form': form})


def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            driver = form.save()
            return redirect('ApxbFleetMain:driver_detail', pk=driver.pk)
    else:
        form = DriverForm(instance=driver)
    return render(request, 'ApxbFleetMain/pages/drivers/edit.html', {'form': form, 'driver': driver})


def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    driver.delete()
    return redirect('driver_list')


def get_driver_behavior_data(request):
    data = DriverBehavior.objects.values(
        'behavior').annotate(count=Count('behavior'))
    data_list = list(data)
    print(len(data_list))
    return JsonResponse({'data': list(data)})


def live_feeds(request):
    return render(request, 'ApxbFleetMain/pages/drivers/livefeeds.html')
