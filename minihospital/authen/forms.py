# forms.py

from django import forms
from .models import Patient
from django.forms.widgets import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'รหัสบัตรประชาชน'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'รหัสผ่าน'
        })
    )

class PatientRegistrationForm(forms.ModelForm):

    PREFIX_CHOICES = (
        ("คำนำหน้า", "คำนำหน้า"),
        ("ด.ญ.", "เด็กหญิง"),
        ("ด.ช.", "เด็กชาย"),
        ("นาย", "นาย"),
        ("น.ส.", "นางสาว"),
        ("นาง", "นาง"), 
    )

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

    GENDER_CHOICES = (
        ('เพศ', 'เพศ'),
        ('ชาย', 'ชาย'),
        ('หญิง', 'หญิง')
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

    prefix = forms.ChoiceField(choices=PREFIX_CHOICES, required=True)
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES, required=True)

    first_name = forms.CharField(
        max_length=255,
        widget=TextInput(attrs={
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'ชื่อ',
        })
    )
    last_name = forms.CharField(
        max_length=255,
        widget=TextInput(attrs={
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'นามสกุล',
        })
    )
    personalID = forms.CharField(
        max_length=13,
        widget=TextInput(attrs={
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'รหัสบัตรประชาชน',
        })
    )
    password = forms.CharField(
        max_length=32,
        widget=PasswordInput(attrs={
            'id': 'password',
            'name': 'password',
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'รหัสผ่าน',
        })
    )
    confirmpassword =  forms.CharField(
        max_length=32,
        widget=PasswordInput(attrs={
            'id': 'password_confirm',
            'name': 'password_confirm',
            'class': 'bg-transparent border-none outline-none',
            'placeholder': 'ยืนยันรหัสผ่าน',
        })
    )

    class Meta:
        model = Patient
        fields = [
            'prefix',
            'first_name',
            'last_name',
            'personalID',
            'gender',
            'password',
            'confirmpassword',
            'nationality',
            'DOB',
            'height',
            'weight',
            'blood_group',
            'phone',
            'address',
            'allergy',
            'patient_image'
        ]

        widgets = {
            "prefix": Select(attrs={
                'class': 'bg-transparent border-none outline-none'
            }),

            "DOB": DateInput(attrs={
                "type": "date",
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'วันเกิด'
            }),

            "phone": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'เบอร์โทร'
            }),
            "gender": Select(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'เพศ'
            }),
            "height": NumberInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'ส่วนสูง'
            }),
            "weight": NumberInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'น้ำหนัก'
            }),
            "blood_group": Select(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'กรุ๊ปเลือด'
            }),
            "allergy": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'ภูมิแพ้'
            }),
            "address": Textarea(attrs={
                'class': 'border-none outline-none bg-[#EAEAEA] rounded-[50px] pl-10 pt-5 flex items-center w-full h-[65px] border-none outline-none text-[#494949]',
                'placeholder': 'ที่อยู่'
            }),
        }

    def clean_personalID(self):
        personalID = self.cleaned_data.get('personalID')
        
        if User.objects.filter(username=personalID).exists():
            raise forms.ValidationError("หมายเลขบัตรประชาชนนี้ตรงกับชื่อผู้ใช้ในระบบ กรุณากรอกหมายเลขใหม่.")
        
        return personalID
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if Patient.objects.filter(phone=phone).exists():
            raise forms.ValidationError('หมายเลขโทรศัพท์นี้ถูกใช้งานแล้ว กรุณากรอกหมายเลขใหม่')
        
        return phone

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmpassword')
        prefix = cleaned_data.get('prefix')
        gender = cleaned_data.get('gender')
        dob = cleaned_data.get('DOB')
        errors = []

        # ตรวจสอบเงื่อนไขที่กำหนด
        if prefix in ['น.ส.', 'นาง', 'ด.ญ.'] and gender != 'หญิง':
            errors.append("สามารถเลือกได้แค่เพศหญิงเท่านั้น !")
        
        if prefix in ['นาย', 'ด.ช.'] and gender != 'ชาย':
            errors.append("สามารถเลือกได้แค่เพศชายเท่านั้น !")

        if password != confirm_password:
            errors.append("รหัสผ่านไม่ตรงกัน !")
        
        if len(password) < 8 and len(confirm_password) < 8:
            errors.append('รหัสผ่านต้องมีอย่างน้อย 8 ตัว')

        if dob > datetime.now().date():
            errors.append("กรุณากรอกวันเกิดใหม่")

        # หากมีข้อผิดพลาด ให้ยกเลิกการส่งฟอร์ม
        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
    