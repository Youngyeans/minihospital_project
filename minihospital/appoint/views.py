from django.shortcuts import render, redirect
from django.views import View
from datetime import date

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
    
        return render(request, 'doctor-list.html')
    
class DoctorAppointmentView(View):

    def get(self, request):
    
        return render(request, 'doctor-list.html')