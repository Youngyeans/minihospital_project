from django.urls import path
from treat.views import TreatmentListView, TreatmentResultView, AppointmentEditView

app_name = 'treat'

urlpatterns = [
    path('treatment/<int:pk>/', TreatmentListView.as_view(), name='treatment-list'),
    path('treatment/<int:user_id>/edit/<int:app_id>/', AppointmentEditView.as_view(), name='appointment_edit'),
    path('treatment/details/<int:pk>/', TreatmentResultView.as_view(), name='treatment-result'),
    
]