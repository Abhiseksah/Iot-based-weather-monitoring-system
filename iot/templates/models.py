from django.db import models
from datetime import datetime

# Create your models here.
class iotdata(models.Model):
    temprature=models.FloatField()
    pressure=models.FloatField()
    altitude=models.FloatField()
    time=models.DateTimeField(default=datetime.now())

class image(models.Model):
    img=models.ImageField(upload_to='pics')
