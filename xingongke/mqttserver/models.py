from django.db import models

# Create your models here.


class MqttData(models.Model):
    topic = models.CharField(max_length=20)
    msg = models.CharField(max_length=60)
