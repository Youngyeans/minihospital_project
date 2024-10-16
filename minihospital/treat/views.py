from django.shortcuts import render, redirect
from django.views import View
from appoint.models import Appointment
from authen.models import Patient
from .models import Treatment, TreatmentType
from django.contrib.auth.models import User

class TreatmentListView(View):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        patient = Patient.objects.get(user=user)

        appointments = Appointment.objects.filter(patient=patient).order_by('-appointment_date')
        treatments = Treatment.objects.filter(appointment__in=appointments)

        print("Appointments:", appointments)
        print("Treatments:", treatments)

        context = {
            'appointments': appointments,
            'treatments': treatments
        }

        return render(request, 'treatment-list.html', context)

class TreatmentResultView(View):

    def get(self, request, pk):
        # user = User.objects.get(pk=pk)
        # patient = Patient.objects.get(user=user)

        appointments = Appointment.objects.filter(pk=pk)
        treatments = Treatment.objects.filter(appointment__in=appointments)

        print("Appointments:", appointments)
        print("Treatments:", treatments)

        context = {
            'appointments': appointments,
            'treatments': treatments,
        }

        return render(request, 'treatment-result.html', context)