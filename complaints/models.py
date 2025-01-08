from django.db import models
from django.contrib.auth import get_user_model
from routes.models import Route


class Complaint(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE, blank=True, null=True)
    waiting_time = models.IntegerField()
