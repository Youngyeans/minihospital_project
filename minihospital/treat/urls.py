from django.urls import path
from treat.views import TreatmentListView, TreatmentResultView

app_name = 'treat'

urlpatterns = [
    path('treatment/<int:pk>', TreatmentListView.as_view(), name='treatment-list'),
    path('treatment/details/<int:pk>', TreatmentResultView.as_view(), name='treatment-result'),
    
]