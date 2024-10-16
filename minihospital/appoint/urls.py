from django.urls import path
from appoint.views import AppointTodayView, DoctorListView, AppointmentView, CreateDoctorView, DoctorAppointmentView, DoctorAppointmentEditView

app_name = 'appoint'

urlpatterns = [
    path("appointment-today/", AppointTodayView.as_view(), name="appoint-today"),
    path("doctor-list/", DoctorListView.as_view(), name="doctor-list"),
    path("createdoctor/", CreateDoctorView.as_view(), name="createdoctor"),
    path("doctor/<int:doctor_id>/appointment/<str:current_date>/", AppointmentView.as_view(), name="appointment"),
    path("doctor_appointment/<str:current_date>/", DoctorAppointmentView.as_view(), name="doc_appointment"),
    path("doctor_appointment/<str:current_date>/<str:appointment_time>/edit/", DoctorAppointmentEditView.as_view(), name="doc_appointment_edit"),
]
