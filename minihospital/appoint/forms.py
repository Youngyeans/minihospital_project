from django.forms import ModelForm
from authen.models import Doctor
from django.forms.widgets import TimeInput, HiddenInput, SelectDateWidget, TextInput
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime, date
from django import forms 
from appoint.models import Appointment


def doc_Schedule():
    min = 10
    updated_times = []
    current_time = datetime.combine(date.today(), datetime.strptime("08:00", "%H:%M").time())
    end_time = datetime.combine(date.today(), datetime.strptime("18:00", "%H:%M").time())

    while current_time < end_time:
        start_time_str = current_time.strftime("%H:%M")
        next_time = current_time + timedelta(minutes=min)
        end_time_str = next_time.strftime("%H:%M")
        current_time = next_time
        time = start_time_str + " - " + end_time_str
        updated_times.append((start_time_str, time))

    return updated_times

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
    appointment_date = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=TextInput(attrs={
            'id': 'startDate',
            'class': 'duration-300 transition ease-in-out delay-150 text-[16px] w-full rounded-full bg-[#EFEFEF] text-[#494949] px-5 py-3 pr-14 focus:outline-none focus:border-[#15cdcb] focus:ring-2 focus:ring-[#15cdcb]',
            'placeholder': 'dd/mm/yyyy',
            'oninput': 'updateDates()',
        })
    )

    start_sympdate = forms.DateField(
        input_formats=['%d/%m/%Y'], 
        widget=TextInput(attrs={
            'id': 'sympDate',
            'class': 'duration-300 transition ease-in-out delay-150 text-[16px] w-full rounded-full bg-[#EFEFEF] text-[#494949] px-5 py-3 pr-14 focus:outline-none focus:border-[#15cdcb] focus:ring-2 focus:ring-[#15cdcb]',
            'placeholder': 'dd/mm/yyyy',
            'required': 'required',
        })
    )

    class Meta:
        model = Appointment
        fields = [
            "appointment_date",
            "appointment_time",
            "symptom",
            "start_sympdate",
            "temperature",
        ]
        widgets = {
            "appointment_time": HiddenInput(),
            'symptom': TextInput(attrs={
                'class': 'w-[500px] py-3 px-6 w-[50%] text-[#c7c7c7] text-base font-normal bg-[#efefef] rounded-full',
                'placeholder': 'เช่น มีไข้ ปวดหัว ตัวร้อน',
                'required': 'required'
            }),
            'temperature': forms.NumberInput(attrs={
                'class': 'py-3 px-6 w-full text-[#c7c7c7] text-base font-normal bg-[#efefef] rounded-full',
                'placeholder': 'เช่น 36.5',
                'step': '0.01',
                'min': '0',
                'required': 'required',
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('appointment_date')
        appointment_time = cleaned_data.get('appointment_time')
        start_sympdate = cleaned_data.get('start_sympdate')
        temperature = float(cleaned_data.get('temperature'))

        if appointment_date and appointment_time:
            appointment_datetime = datetime.combine(appointment_date, appointment_time)

            if appointment_datetime < datetime.now():
                raise forms.ValidationError('วันและเวลาที่จองต้องไม่เป็นอดีต')
            
        if not start_sympdate:
            raise forms.ValidationError('กรุณากรอกวันที่เริ่มมีอาการ')
        else:
            if start_sympdate > appointment_date:
                raise forms.ValidationError('วันที่เริ่มมีอาการควรเป็นอดีต')
        
        if temperature > 37.2 or temperature < 36.1:
            raise forms.ValidationError('อุณหภูมิร่างกายควรอยู่ในช่วงระหว่าง 36.1-37.2 องศาเซลเซียส')

        return cleaned_data
    

class AppointmentEditForm(ModelForm):
    appointment_date = forms.DateField(
        widget=SelectDateWidget(attrs={
            'class': 'rounded-[20px] bg-[#EFEFEF] text-[#494949] px-5 py-2 focus:outline-none focus:border-[#15cdcb] focus:ring-2 focus:ring-[#15cdcb]',
        })
    )

    appointment_time = forms.ChoiceField(
        choices=doc_Schedule(), 
        widget=forms.Select(attrs={
        'class': 'py-3 px-5 text-base font-normal bg-[#EFEFEF] rounded-full',
        'required': 'required',
    }))

    class Meta:
        model = Appointment
        fields = [
            "appointment_date",
            "appointment_time",
        ]

    def clean(self):
        cleaned_data = super().clean()
        appointment_date = cleaned_data.get('appointment_date')
        print(f"appointment_date = {appointment_date}")
        appointment_time = cleaned_data.get('appointment_time')
        print(f"appointment_time = {appointment_time}") 

        if appointment_date and appointment_time:
            appointment_datetime = datetime.combine(appointment_date, datetime.strptime(appointment_time, "%H:%M").time())

            if appointment_datetime < datetime.now():
                raise forms.ValidationError('วันและเวลาที่จองต้องไม่เป็นอดีต')
            

