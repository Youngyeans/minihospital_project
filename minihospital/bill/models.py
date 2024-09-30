from django.db import models
from appoint.models import Appointment

class Invoice(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Invoice {self.id}'