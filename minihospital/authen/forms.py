# forms.py

from django import forms
from .models import Patient
from django.forms.widgets import *

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
    first_name = forms.CharField(max_length=225)
    last_name = forms.CharField(max_length=225)
    personalID = forms.CharField(max_length=13)
    password = forms.CharField(max_length=32)
    confirmpassword = forms.CharField(max_length=32)

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
            "password": PasswordInput(attrs={
                'id': 'password',
                'name': 'password',
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'รหัสผ่าน',
            }),
            "confirmpassword": PasswordInput(attrs={
                'id': 'password',
                'name': 'password',
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'รหัสผ่าน'
            }),
            "prefix": Select(attrs={
                'class': 'bg-transparent border-none outline-none'
            }),
            "first_name": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'ชื่อ'
            }),
            "last_name": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'นามสกุล'
            }),
            "DOB": DateInput(attrs={
                "type": "date",
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'วันเกิด'  # Optional placeholder
            }),
            "personalID": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'รหัสบัตรประชาชน'
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
            "password": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'รหัสผ่าน'
            }),
            "confirmpassword": TextInput(attrs={
                'class': 'bg-transparent border-none outline-none',
                'placeholder': 'ยืนยันรหัสผ่าน'
            }),
            # "patient_image": URLInput(attrs={
            #     'class': 'absolute opacity-0 cursor-pointer',
            #     'type' : 'url'
            # })

        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['patient_image'].widget.attrs.update({
            'style': 'opacity: 0; position: absolute; top: 25px; left:-8px; cursor: pointer; z-index: 10;',
            'onchange': 'onchange="previewImage(event)'  # Replace with your actual function
        })

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirmpassword')

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match!")
        
        return cleaned_data