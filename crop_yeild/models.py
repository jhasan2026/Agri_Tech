from django.db import models

# Create your models here.

class TemperatureHumidity(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Temp: {self.temperature}, Humidity: {self.humidity}"


