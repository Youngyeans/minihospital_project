from django.urls import path
from patient.views import ProfileView, ProfileEditView

app_name = 'patient'

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profiletest/', ProfileEditView.as_view(), name='profile-edit'),
    
]