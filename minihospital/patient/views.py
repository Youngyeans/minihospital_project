from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from authen.models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, View):
    login_url = 'authen:login'
    def profile_view(request):
        # ดึงข้อมูล Patient ที่เชื่อมโยงกับผู้ใช้ปัจจุบัน
        try:
            patient = Patient.objects.get(user=request.user)  # ใช้ request.user เพื่อดึงข้อมูลของผู้ใช้ที่ล็อกอิน
        except Patient.DoesNotExist:
            patient = None

        context = {
            'patient': patient  # ส่งข้อมูล patient ไปยังเทมเพลต
        }
        return render(request, 'profile.html', context)
class ProfileEditView(View):

    def get(self, request):
        return render(request, 'profile-edit.html')
    