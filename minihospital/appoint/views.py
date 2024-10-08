from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from .forms import DoctorForm
from authen.models import Doctor

class AppointTodayView(View):

    def get(self, request):
        doctor_list = range(9)
        today = date.today() 
        context ={
            'doctor_list': doctor_list,
            'today': today,
        }
        return render(request, 'appointment-today.html', context)
    
class DoctorListView(View):

    def get(self, request):
        doctor_list = Doctor.objects.all().order_by('id')
        id_last = Doctor.objects.last().id
        context={
            "doctor_list": doctor_list,
            "id_last": id_last
        }
        return render(request, 'doctor-list.html', context)
    

class CreateDoctorView(View):

    def get(self, request):
        form = DoctorForm()
        context={
            "form": form,
        }
        return render(request, 'create_doctor.html', context)
    
    def post(self, request):
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctor-list')

        return render(request, "create_doctor.html", {
            "form": form
        })
    
class DoctorAppointmentView(View):

    def get(self, request):
    
        return render(request, 'doctor-list.html')