from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from .forms import DoctorForm
from authen.models import Doctor
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, Group

class AppointTodayView(View):

    def get(self, request):
        doctor_list = range(9)
        today = date.today().strftime("%d/%m/%Y")   
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
            "id_last": id_last,
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
            try:
                with transaction.atomic():
                    doc = form.save(commit=False)
                    User.objects.create_user(
                            username= form.cleaned_data["personalID"],
                            password="Xy7#p9Tk!",
                            first_name= form.cleaned_data["first_name"],
                            last_name= form.cleaned_data["last_name"],
                            email= form.cleaned_data["email"]
                        )
                    
                    user = authenticate(
                        request,
                        username= form.cleaned_data["personalID"],
                        password="Xy7#p9Tk!"
                    )

                    doctor_group = Group.objects.get(name='doctor')
                    user.groups.add(doctor_group)
                    
                    doc.user = user
                    doc.save()

            except ObjectDoesNotExist:
                print("ไม่มีบัญชีหมอคนนี้")
            return redirect('appoint:doctor-list')

        return render(request, "create_doctor.html", {
            "form": form
        })
    
class DoctorAppointmentView(View):

    def get(self, request):
        today = date.today() 
        week = range(7)
        context ={
            'week' : week,
            'today': today,
        }
        return render(request, 'appointment.html', context)