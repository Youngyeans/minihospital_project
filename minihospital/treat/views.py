from django.shortcuts import render, redirect
from django.views import View
from appoint.models import Appointment
from authen.models import Patient
from .models import Treatment, TreatmentType
from django.contrib.auth.models import User
from django.db.models import Count
from .forms import AppointmentEditForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def doc_appoint(doc, appointment_date):
    appointments = Appointment.objects.filter(doctor=doc, appointment_date=appointment_date)
    appoint_time = [
        appointment_time.strftime('%H:%M') for appointment_time in appointments.values_list('appointment_time', flat=True)
    ]

    return appoint_time

def patient_appoint(patient, appointment_date):
    appointments = Appointment.objects.filter(patient=patient, appointment_date=appointment_date)
    appoint_time = [
        appointment_time.strftime('%H:%M') for appointment_time in appointments.values_list('appointment_time', flat=True)
    ]

    return appoint_time


class TreatmentListView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'authen:login'
    permission_required = ["treat.view_treatment"]

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        patient = Patient.objects.get(user=user)

        appointments = Appointment.objects.filter(patient=patient).annotate(treat_count=Count('treatment')).order_by('-id')
        treatments = Treatment.objects.filter(appointment__in=appointments)

        for app in appointments:
            print(f"Appointment ID: {app.id}, Number of Treatments: {app.treat_count}")


        print("Appointments:", appointments)
        print("Treatments:", treatments)

        context = {
            'appointments': appointments,
            'treatments': treatments
        }

        return render(request, 'treatment-list.html', context)

class TreatmentResultView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'authen:login'
    permission_required = ["treat.view_treatment"]

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
    
class AppointmentEditView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'authen:login'
    permission_required = ["appoint.change_appointment", "appoint.delete_appointment"]

    def get(self, request, user_id, app_id):
        user = User.objects.get(pk=user_id)
        patient = Patient.objects.get(user=user)

        appointments = Appointment.objects.filter(patient=patient).annotate(treat_count=Count('treatment')).order_by('-appointment_date')
        treatments = Treatment.objects.filter(appointment__in=appointments)

        app = Appointment.objects.get(pk=app_id)
        doc =  app.doctor

        initial_data = {
            'appointment_time': app.appointment_time.strftime("%H:%M")
        }
    
        form = AppointmentEditForm(instance=app, initial=initial_data)

        context = {
            'appointments': appointments,
            'treatments': treatments,
            'app': app,
            'doc': doc,
            'form': form
        }
        return render(request, 'appointment_edit.html', context)
    
    def post(self, request, user_id, app_id):
        user = User.objects.get(pk=user_id)
        patient = Patient.objects.get(user=user)

        appointments = Appointment.objects.filter(patient=patient).annotate(treat_count=Count('treatment')).order_by('-appointment_date')
        treatments = Treatment.objects.filter(appointment__in=appointments)

        app = Appointment.objects.get(pk=app_id)
        doc =  app.doctor
    
        form = AppointmentEditForm(request.POST, instance=app)

        context = {
            'appointments': appointments,
            'treatments': treatments,
            'app': app,
            'doc': doc,
            'form': form
        }

        if form.is_valid():
            try:
                with transaction.atomic():
                    appoint = form.save(commit=False)
                    appointment_time = form.cleaned_data["appointment_time"]
                    appointment_date = form.cleaned_data["appointment_date"]
                    appoint_time = doc_appoint(doc, appointment_date) + patient_appoint(request.user.patient, appointment_date)
                    print(f"appoint_time = {appoint_time}")

                    if appointment_time in appoint_time:
                        form.add_error('appointment_time', 'มีนัดแล้วในเวลานี้ กรุณาเลือกเวลาอื่น')
                        return render(request, 'appointment_edit.html', context)
                    else:
                        print("update appointment")
                        appoint.save()
                        return redirect('treat:treatment-list' ,pk=request.user.id)

            except ObjectDoesNotExist:
                print("ไม่มีสามารถแก้ไขนัดหมายได้")

        return render(request, 'appointment_edit.html', context)
    
    def delete(self, request, user_id, app_id):
        try:
            app = Appointment.objects.get(pk=app_id)
            app.delete()
            return JsonResponse({'message': 'Appointment deleted successfully'}, status=200)
        except Appointment.DoesNotExist:
            return JsonResponse({'error': 'Appointment not found'}, status=404)
