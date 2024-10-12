from django.urls import path
from appoint.views import AppointTodayView, DoctorListView, AppointmentView, CreateDoctorView, DoctorAppointmentView

app_name = 'appoint'

urlpatterns = [
    path("appointment-today/", AppointTodayView.as_view(), name="appoint-today"),
    path("doctor-list/", DoctorListView.as_view(), name="doctor-list"),
    path("createdoctor/", CreateDoctorView.as_view(), name="createdoctor"),
    path("doctor/<int:doctor_id>/appointment/", AppointmentView.as_view(), name="appointment"),
    path("doctor_appointment/", DoctorAppointmentView.as_view(), name="doc_appointment"),
]