from django.shortcuts import render, redirect
from django.views import View

class AppointTodayView(View):

    def get(self, request):
        return render(request, 'appointment-today.html')
    
class DoctorListView(View):

    def get(self, request):
    
        return render(request, 'doctor-list.html')
    
class DoctorAppointmentView(View):

    def get(self, request):
    
        return render(request, 'doctor-list.html')