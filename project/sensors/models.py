from django.db import models

class SensorData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    rain = models.FloatField()
    light = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.timestamp} - Rain: {self.rain}, Light: {self.light}, Humidity: {self.humidity}, Temperature: {self.temperature}"
