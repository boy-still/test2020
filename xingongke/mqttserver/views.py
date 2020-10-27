from django.shortcuts import render
from django.http import HttpResponse
from module import mqtt_function
from . import models
# Create your views here.


def mqttserver(request):
    return HttpResponse("Hello world")


def test(request):
    mqtt_function.mqtt_run()
    context = {'topic': models.MqttData.objects.values('topic').distinct(),'msg':models.MqttData.objects.values('msg')[len(models.MqttData.objects.values('msg'))-1]}
    return render(request, 'app_index.html', context=context)
