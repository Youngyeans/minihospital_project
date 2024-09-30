from django.db import models
from appoint.models import Appointment

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    prescriptionDetail = models.TextField(null=True)
    prescriptionDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Prescription {self.id}'
    
class Medicine(models.Model):
    class Type(models.Choices):
        Water = "ยาน้ำ"
        Solid = "ยาเม็ด"
        Capsule = "แคปซูล"
        Cream = "ยาทา"
    name = models.CharField(max_length=255)
    type = models.CharField(choices=Type.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stockQuantity = models.IntegerField()
    expiryDate = models.DateField()
    instruction = models.TextField()

    def __str__(self):
        return self.name

class PrescriptionMedicines(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.medicine.name} in Prescription {self.prescription.id}'
