from django.forms import ModelForm
from authen.models import Doctor
from django.forms.widgets import TimeInput
from django.core.exceptions import ValidationError
from datetime import timedelta, datetime, date
from django import forms 

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
