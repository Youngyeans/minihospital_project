from django.urls import path
from treat.views import TreatmentListView, TreatmentResultView

app_name = 'treat'

urlpatterns = [
    path('treatment/', TreatmentListView.as_view(), name='treatment-list'),
    path('treatmenttest/', TreatmentResultView.as_view(), name='treatment-result'),
    
]