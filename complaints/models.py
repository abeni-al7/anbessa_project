from django.db import models
from django.contrib.auth import get_user_model


class Complaint(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    current_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    waiting_time = models.IntegerField()
