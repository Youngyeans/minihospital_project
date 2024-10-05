from django.shortcuts import render, redirect
from django.views import View

class AppointTodayView(View):

    def get(self, request):
        doctor_list = range(5)
        return render(request, 'appointment-today.html', {'doctor_list': doctor_list})
    
class DoctorListView(View):

    def get(self, request):
    
        return render(request, 'doctor-list.html')
    
class DoctorAppointmentView(View):

    def get(self, request):
    
        return render(request, 'doctor-list.html')