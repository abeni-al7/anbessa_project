from django.db import models


class Route(models.Model):
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    distance = models.FloatField()
    duration = models.FloatField()
    bus_number = models.CharField(max_length=10)
    bus_stops = models.TextField()

    def __str__(self):
        return f'{self.start_location} to {self.end_location}'
