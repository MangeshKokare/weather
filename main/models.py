from django.db import models

# Create your models here.
# models.py


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    temperature = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()

# models.py

from django.db import models

class WeatherSearchHistory(models.Model):
    city = models.CharField(max_length=100)
    coordinate = models.CharField(max_length=30)
    country_code = models.CharField(max_length=10)
    temperature = models.CharField(max_length=30)
    pressure = models.CharField(max_length=30)
    humidity = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.timestamp}"
