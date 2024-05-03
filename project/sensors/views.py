from django.shortcuts import render
from django.http import Http404
from .models import SensorData

# Create your views here
def index(request):
    try:
        datasets = SensorData.objects.all().order_by('-timestamp')

        data = {
            'labels': [data.timestamp.strftime('%Y-%m-%d %H:%M:%S') for data in datasets],
            'rain': [data.rain for data in datasets],
            'light': [data.light for data in datasets],
            'humidity': [data.humidity for data in datasets],
            'temperature': [data.temperature for data in datasets],
        }
    except:
        raise Http404("No sensors exist")
    
    return render(request, 'sensors/sensors.html', {'data':data})

def logs(request):
    try:
        data = SensorData.objects.all().order_by('-timestamp')
    except:
        raise Http404("No logs exist")
    
    return render(request, 'sensors/logs.html', {'data':data})