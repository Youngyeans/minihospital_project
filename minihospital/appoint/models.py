from django.db import models
# from authen.models import Patient, Doctor
from django.contrib.auth.models import User

class Appointment(models.Model):
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    symptom = models.TextField()
    start_sympDate = models.DateField()
    temperature = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Appointment {self.id}'