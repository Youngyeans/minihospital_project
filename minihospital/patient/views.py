from django.shortcuts import render, redirect
from django.views import View

class ProfileView(View):

    def get(self, request):
        return render(request, 'profile-patient.html')

class ProfileEditView(View):

    def get(self, request):
        return render(request, 'profile-edit.html')
    