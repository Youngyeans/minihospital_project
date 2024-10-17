# forms.py

from django import forms
from authen.models import Patient, User
from django.forms.widgets import *
    
class PatientEditProfileForm(forms.ModelForm):
    NATIONALITY_CHOICES = (
        ("สัญชาติ", 'สัญชาติ'),
        ("ไทย", "ไทย"),
        ("อเมริกัน", "อเมริกัน"),
        ("อังกฤษ", "อังกฤษ"),
        ("ญี่ปุ่น", "ญี่ปุ่น"),
        ("จีน", "จีน"),
        ("อินเดีย", "อินเดีย"),
        ("ฝรั่งเศส", "ฝรั่งเศส"),
        ("เยอรมัน", "เยอรมัน"),
        ("ออสเตรเลีย", "ออสเตรเลีย"),
        ("แคนาดา", "แคนาดา"),
        ("เกาหลี", "เกาหลี"),
        ("เวียดนาม", "เวียดนาม"),
        ("มาเลเซีย", "มาเลเซีย"),
        ("สิงคโปร์", "สิงคโปร์"),
        ("พม่า", "พม่า"),
        ("ลาว", "ลาว"),
        ("กัมพูชา", "กัมพูชา"),
        ("ฟิลิปปินส์", "ฟิลิปปินส์"),
        ("บราซิล", "บราซิล"),
        ("รัสเซีย", "รัสเซีย"),
    )

    BLOOD_GROUP_CHOICES = (
        ('กรุ๊ปเลือด', 'กรุ๊ปเลือด'),
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-")
    )

    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES)
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)

    class Meta:
        model = Patient
        fields = [
            'gender',
            'nationality',
            'height',
            'weight',
            'blood_group',
            'phone',
            'address',
            'allergy',
            'patient_image'
        ]

        widgets = {
            "phone": TextInput(attrs={
                'class': 'h-8 border-b-2 border-gray-300 focus:outline-none focus:border-black ',
                'placeholder': 'เบอร์โทร'
            }),
            "gender": Select(attrs={
                'class': 'h-8 border-b-2 border-gray-300 focus:outline-none focus:border-black',
                'placeholder': 'เพศ'
            }),
            "height": NumberInput(attrs={
                'class': 'h-8 border-b-2 border-gray-300 focus:outline-none focus:border-black ',
                'placeholder': 'ส่วนสูง'
            }),
            "weight": NumberInput(attrs={
                'class': 'h-8 border-b-2 border-gray-300 focus:outline-none focus:border-black',
                'placeholder': 'น้ำหนัก'
            }),
            "blood_group": Select(attrs={
                'class': 'h-8 border-b-2 border-gray-300 focus:outline-none focus:border-black ',
                'placeholder': 'กรุ๊ปเลือด'
            }),
            "allergy": TextInput(attrs={
                'class': 'h-8 border-b-2 border-gray-300 focus:outline-none focus:border-black',
                'placeholder': 'ภูมิแพ้'
            }),
            "address": Textarea(attrs={
                'class': 'border-b-2 border-gray-300 focus:outline-none focus:border-black',
                'placeholder': 'ที่อยู่'
            }),
        }
    
    