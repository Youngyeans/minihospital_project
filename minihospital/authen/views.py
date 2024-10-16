import json
from decimal import Decimal
from django.shortcuts import render, redirect
from django.views import View
from .models import Patient
from .forms import PatientRegistrationForm, CustomAuthenticationForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth import logout, login, authenticate
from django.db import transaction
from django.contrib.auth.models import User, Group
import json
from django.contrib.auth.forms import AuthenticationForm

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()

        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = CustomAuthenticationForm()
        current = datetime.now()
        current_date = current.strftime('%Y-%m-%d')
        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            if  hasattr(user, 'doctor'):
                return redirect('appoint:doc_appointment', current_date=current_date)
            else:
                return redirect('main:home')

        messages.error(request, 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง!')
        return render(request, 'login.html', {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('authen:login')

class RegisterView(View):
    def get(self, request):
        referrer = request.META.get('HTTP_REFERER')

        if referrer and "validation" in referrer:
            # ดึงข้อมูลจากเซสชันพร้อมแปลงกลับมาเป้น python objects
            registration_data_json = request.session.get('registration_data', {})
            registration_data = json.loads(registration_data_json)
            form = PatientRegistrationForm(initial=registration_data)
        else:
            form = PatientRegistrationForm()

        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = PatientRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            context = {
                'prefix': form.cleaned_data['prefix'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'personalID': form.cleaned_data['personalID'],
                'nationality': form.cleaned_data['nationality'],
                'password': form.cleaned_data['password'],
                'confirmpassword': form.cleaned_data['confirmpassword'],
                'phone': form.cleaned_data['phone'],
                'gender': form.cleaned_data['gender'],
                'DOB': form.cleaned_data['DOB'].strftime('%Y-%m-%d'),
                'height': str(form.cleaned_data['height']),
                'weight': str(form.cleaned_data['weight']),
                'blood_group': form.cleaned_data['blood_group'],
                'allergy': form.cleaned_data['allergy'],
                'address': form.cleaned_data['address'],
            }
            json_data = json.dumps(context)
            request.session['registration_data'] = json_data

            return redirect('authen:validation')
        
        context = {
                'form': form,
            }
        
        return render(request, 'register.html', context)

class ValidationView(View):
    def get(self, request):
        registration_data_json = request.session.get('registration_data', {})
        if registration_data_json is None:
            messages.error(request, "ไม่พบข้อมูลการลงทะเบียน")
            return redirect('authen:register')

        registration_data = json.loads(registration_data_json)
  
        return render(request, 'validation.html', registration_data)

    def post(self, request):
        if 'save' in request.POST:
            registration_data_json = request.session.get('registration_data', None)
            if registration_data_json is None:
                messages.error(request, "ไม่พบข้อมูลการลงทะเบียน")
                return redirect('authen:register')

            registration_data = json.loads(registration_data_json)

            #สร้างบัญชีและ User 
            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=registration_data['personalID'],
                        password=registration_data['password'],
                        first_name=registration_data['first_name'],
                        last_name=registration_data['last_name'],
                    )

                    patient = Patient(
                        prefix=registration_data['prefix'],
                        nationality=registration_data['nationality'],
                        phone=registration_data['phone'],
                        gender=registration_data['gender'],
                        DOB=datetime.strptime(registration_data['DOB'], '%Y-%m-%d').date(),
                        height=Decimal(registration_data['height']),
                        weight=Decimal(registration_data['weight']),
                        blood_group=registration_data['blood_group'],
                        allergy=registration_data['allergy'],
                        address=registration_data['address'],
                        user=user
                    )

                    patient_group = Group.objects.get(pk=2)
                    patient_group.user_set.add(user)

                    patient.save()
                    messages.success(request, "ลงทะเบียนสำเร็จ !")

            except Exception:
                messages.error(request, "ลงทะเบียนไม่สำเร็จ !")
                return redirect('authen:register')

            del request.session['registration_data']
            return redirect('authen:login')

        elif 'cancel' in request.POST:
            return redirect('authen:register')
