from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver
from .forms import DriverForm
# Create your views here.


def index(request) -> HttpResponse:
    return render(request, 'ApxbFleetMain/index.html')


def login(request) -> HttpResponse:
    return render(request, 'ApxbFleetMain/login.html')


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'ApxbFleetMain/pages/drivers/index.html', {'drivers': drivers})


def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'ApxbFleetMain/pages/drivers/details.html', {'driver': driver})


def create_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ApxbFleetMain/pages/drivers/index.html')
    else:
        form = DriverForm()

    return render(request, 'ApxbFleetMain/pages/drivers/add.html', {'form': form})


def driver_edit(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            driver = form.save(commit=False)
            driver.save()
            return redirect('driver_detail', pk=driver.pk)
    else:
        form = DriverForm(instance=driver)
    return render(request, 'drivers/driver_edit.html', {'form': form})


def driver_delete(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    driver.delete()
    return redirect('driver_list')
