from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
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
            

