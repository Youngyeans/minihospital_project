from django.forms import ModelForm
from authen.models import Doctor
from django.forms.widgets import TimeInput, HiddenInput, NumberInput, TextInput
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime, date
from django import forms 
from appoint.models import Appointment

class DoctorForm(ModelForm):
    first_name = forms.CharField(max_length=225)
    last_name = forms.CharField(max_length=225)
    email = forms.EmailField()
    personalID = forms.CharField(max_length=13)

    class Meta:
        model = Doctor
        fields = [
            "prefix",
            "first_name",
            "last_name",
            "phone",
            "email",
            "personalID",
            "address",
            "department",
            "doctor_image",
            "shift_day",
            "start_time",
            "end_time",
            "description"
        ]
        widgets = {
            "start_time": TimeInput(attrs={'type': 'time'}),
            "end_time": TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'border border-black', 'style' : 'background-color: transparent;'})

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:

            time_difference = datetime.combine(date.min, end_time) - datetime.combine(date.min, start_time)

            if time_difference <= timedelta(0):
                raise ValidationError("end_time must be greater than start_time")
            
            if time_difference < timedelta(hours=4):
                raise ValidationError("time range must be at least 4 hours.")

        return cleaned_data
    

class AppointmentForm(ModelForm):

    class Meta:
        model = Appointment
        fields = [
            "appointment_date",
            "appointment_time",
            "symptom",
            "start_sympDate",
            "temperature",
        ]
        widgets = {
            "appointment_time": HiddenInput(),
            'appointment_date': TextInput(attrs={
                'id': 'startDate',
                'class': 'duration-300 transition ease-in-out delay-150 text-[16px] w-full rounded-full bg-[#EFEFEF] text-[#494949] px-5 py-3 pr-14 focus:outline-none focus:border-[#15cdcb] focus:ring-2 focus:ring-[#15cdcb]',
                'placeholder': 'dd/mm/yyyy',
                'oninput': 'updateDates()',
            }),
            'symptom': TextInput(attrs={
                'class': 'w-[500px] py-3 px-6 w-[50%] text-[#c7c7c7] text-base font-normal bg-[#efefef] rounded-full',
                'placeholder': 'เช่น มีไข้ ปวดหัว ตัวร้อน',
            }),
            'start_sympDate': TextInput(attrs={
                'id': 'sympDate',
                'class': 'duration-300 transition ease-in-out delay-150 text-[16px] w-full rounded-full bg-[#EFEFEF] text-[#494949] px-5 py-3 pr-14 focus:outline-none focus:border-[#15cdcb] focus:ring-2 focus:ring-[#15cdcb]',
                'placeholder': 'dd/mm/yyyy',
            }),
            'temperature': NumberInput(attrs={
                'class': 'py-3 px-6 w-full text-[#c7c7c7] text-base font-normal bg-[#efefef] rounded-full',
                'placeholder': 'เช่น 36.5',
                'step': '0.01',  # ระบุ step เพื่อกำหนดค่าที่เพิ่มทีละ 0.01
                'min': '0', 
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # กำหนดค่าเริ่มต้นสำหรับ appointment_date เป็นวันที่ปัจจุบัน
        if 'initial' not in kwargs:
            self.fields['appointment_date'].initial = date.today().strftime('%d/%m/%Y')

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('appointment_date')
        appointment_time = cleaned_data.get('appointment_time')

        if appointment_date and appointment_time:
            appointment_datetime = datetime.combine(appointment_date, appointment_time)
            
            if appointment_datetime < datetime.now():
                raise forms.ValidationError('ไม่สามารถเลือกวันที่และเวลาย้อนหลังได้')

        return cleaned_data