from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Patient(models.Model):
    class Prefix(models.Choices):
        girl = "ด.ญ."
        boy = "ด.ช."
        male = "นาย"
        female = "น.ส."
        wife = "นาง"

    class Gender(models.Choices):
        M = "ชาย"
        F = "หญิง"

    class Nationality(models.TextChoices):
        THAI = "ไทย"
        AMERICAN = "อเมริกัน"
        BRITISH = "อังกฤษ"
        JAPANESE = "ญี่ปุ่น"
        CHINESE = "จีน"
        INDIAN = "อินเดีย"
        FRENCH = "ฝรั่งเศส"
        GERMAN = "เยอรมัน"
        AUSTRALIAN = "ออสเตรเลีย"
        CANADIAN = "แคนาดา"
        KOREAN = "เกาหลี"
        VIETNAMESE = "เวียดนาม"
        MALAYSIAN = "มาเลเซีย"
        SINGAPOREAN = "สิงคโปร์"
        MYANMAR = "พม่า"
        LAO = "ลาว"
        CAMBODIAN = "กัมพูชา"
        FILIPINO = "ฟิลิปปินส์"
        BRAZILIAN = "บราซิล"
        RUSSIAN = "รัสเซีย"

    class BloodGroup(models.TextChoices):
        A_POSITIVE = "A+"
        A_NEGATIVE = "A-"
        B_POSITIVE = "B+"
        B_NEGATIVE = "B-"
        AB_POSITIVE = "AB+"
        AB_NEGATIVE = "AB-"
        O_POSITIVE = "O+"
        O_NEGATIVE = "O-"

    prefix = models.CharField(choices=Prefix.choices)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    personalID = models.CharField(max_length=13, unique=True)
    gender = models.CharField(choices=Gender.choices)
    nationality = models.CharField(choices=Nationality.choices)
    DOB = models.DateField()
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    blood_group = models.CharField(choices=BloodGroup.choices)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    allergy = models.TextField(blank=True, null=True)
    registrationDate = models.DateField(auto_now_add=True)
    patient_image = models.ImageField(upload_to='images/patient/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Doctor(models.Model):
    prefix = models.CharField(max_length=10, default='นพ.')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    doctor_image = models.ImageField(upload_to="images/doctor/", blank=True, null=True)
    shift_day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    personalID = models.CharField(max_length=13, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# password : Xy7#p9Tk!
    
class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
