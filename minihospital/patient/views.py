from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from authen.models import Patient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from patient.forms import PatientEditProfileForm


class ProfileView(LoginRequiredMixin, View):
    login_url = 'authen:login'
    def get(self, request, pk):
        # ดึงข้อมูล User ที่เชื่อมโยงกับผู้ใช้ปัจจุบัน
        user = User.objects.get(pk=pk)  # ค้นหา User ตาม pk ที่ส่งมา
        # ดึงข้อมูล Patient ที่เชื่อมโยงกับ User
        patient = Patient.objects.get(user=user)
        context = {
            'user': user,       # ส่งข้อมูล User ไปยังเทมเพลต
            'patient': patient, # ส่งข้อมูล Patient ไปยังเทมเพลต
        }
        
        return render(request, 'profile-patient.html', context)
    
    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        return redirect('patient:profile-edit', pk=user.pk)
    
class ProfileEditView(LoginRequiredMixin, View):
    login_url = 'authen:login'

    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        patient = Patient.objects.get(user=user)
        form = PatientEditProfileForm(instance=patient)  # ใช้ฟอร์มจาก authen.forms
        
        context = {
            'user': user,
            'patient': patient,
            'form': form,
        }
        
        return render(request, 'profile-edit.html', context)
    
    def post(self, request, pk):
        if 'save' in request.POST:
            user = User.objects.get(pk=pk)
            patient = Patient.objects.get(user=user)
            form = PatientEditProfileForm(request.POST, request.FILES, instance=patient)

            new_phone = request.POST.get('phone')

            if Patient.objects.exclude(user=user).filter(phone=new_phone).exists():
                messages.error(request, "กรุณากรอกเบอร์ใหม่")
                return render(request, 'profile-edit.html', {'form': form, 'user': user, 'patient': patient})

            if form.is_valid():
                form.save()  # Save the updated patient information
                return redirect('patient:profile', pk=user.pk)  # Redirect to profile page after saving
            else:
                print(form.errors)  # เพื่อดูข้อผิดพลาด

        elif 'cancel' in request.POST:
            user = User.objects.get(pk=pk)
            return redirect('patient:profile', pk=user.pk)