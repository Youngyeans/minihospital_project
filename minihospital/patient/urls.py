from django.urls import path
from patient.views import ProfileView, ProfileEditView

app_name = 'patient'

urlpatterns = [
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),
    
]