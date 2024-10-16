from django.db import models
from appoint.models import Appointment

class TreatmentType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Treatment(models.Model):
    treatment_type = models.ForeignKey(TreatmentType, on_delete=models.CASCADE)
    details = models.TextField()
    diagnose = models.TextField(null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    def __str__(self):
        return f'Treatment {self.id}'