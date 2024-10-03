from django.urls import path
from appoint.views import AppointTodayView, DoctorListView, DoctorAppointmentView

urlpatterns = [
    path("appointment-today/", AppointTodayView.as_view(), name="appoint-today"),
    path("doctor-list/", DoctorListView.as_view(), name="doctor-list"),
    path("doctor/appointment/", DoctorAppointmentView.as_view(), name="appointment"),
]