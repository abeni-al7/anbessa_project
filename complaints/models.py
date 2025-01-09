from django.db import models
from django.contrib.auth import get_user_model
from routes.models import Route


class Complaint(models.Model):
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    route_id = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="complaints",
        blank=True,
        null=True,
    )
    waiting_time = models.IntegerField()

    def __str__(self):
        return f"Complaint {self.user_id} - {self.route_id} - {self.date}"
