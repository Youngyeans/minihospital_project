import json
from decimal import Decimal
from django.shortcuts import render, redirect
from django.views import View
from .models import Patient
from .forms import PatientRegistrationForm, CustomAuthenticationForm
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth.models import User, Group
from django.core.files.uploadedfile import InMemoryUploadedFile
import json
from io import BytesIO
from PIL import Image
import base64
from .serializers import PatientSerializer

class LoginView(View):
    def get(self, request):
        form = CustomAuthenticationForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:home')
        else:
            # ตรวจสอบข้อผิดพลาดในฟอร์ม
            print(form.errors)  # สำหรับการดีบัก

        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('authen:login')

class RegisterView(View):
    def get(self, request):
        referrer = request.META.get('HTTP_REFERER')

        if referrer and "validation" in referrer:
            # ดึงข้อมูลจากเซสชันพร้อมแปลงกลับมาเป้น python dictionary
            registration_data_json = request.session.get('registration_data', {})
            registration_data = json.loads(registration_data_json)

            form = PatientRegistrationForm(initial=registration_data)
        else:
            form = PatientRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = PatientRegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            patient_image = form.cleaned_data.get('patient_image')
            if patient_image:
                try:
                    image_buffer = BytesIO()
                    image = Image.open(patient_image)
                    image.save(image_buffer, format='PNG')
                    image_data = image_buffer.getvalue()
                    base64_image = base64.b64encode(image_data).decode('utf-8')
                    request.session['patient_image'] = base64_image
                except Exception:
                    messages.error(request, "Error processing image. Please try again.")
                    return render(request, 'register.html', {'form': form})

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
                'DOB': form.cleaned_data['DOB'].strftime('%Y-%m-%d'),  # Convert date to string
                'height': str(form.cleaned_data['height']),
                'weight': str(form.cleaned_data['weight']),
                'blood_group': form.cleaned_data['blood_group'],
                'allergy': form.cleaned_data['allergy'],
                'address': form.cleaned_data['address'],
            }
            json_data = json.dumps(context)
            request.session['registration_data'] = json_data
            return redirect('authen:validation')
        else:
            # ฟอร์มไม่ valid ให้ดึงข้อมูลรูปภาพจากเซสชันมาแสดงใหม่
            base64_image = request.session.get('patient_image')
            if base64_image:
                form.fields['patient_image'].initial = base64_image

            # เก็บข้อมูลที่กรอกไว้กลับในฟอร์ม
            context = {
                'form': form,
                'base64_image': base64_image
            }

            # แสดงข้อผิดพลาด
            print(form.errors)  # สำหรับการดีบัก
        
        return render(request, 'register.html', context)

class ValidationView(View):
    def get(self, request):
        registration_data_json = request.session.get('registration_data', None)
        if registration_data_json is None:
            messages.error(request, "No registration data found.")
            return redirect('authen:register')

        registration_data = json.loads(registration_data_json)
        base64_image = request.session.get('patient_image', None)

        context = {**registration_data, 'base64_image': base64_image}
        return render(request, 'validation.html', context)

    def post(self, request):
        if 'save' in request.POST:
            registration_data_json = request.session.get('registration_data', None)
            if registration_data_json is None:
                messages.error(request, "No registration data found.")
                return redirect('authen:register')

            registration_data = json.loads(registration_data_json)
            base64_image = request.session.get('patient_image', None)

            if base64_image:
                image_data = base64.b64decode(base64_image)
                image_temp_file = InMemoryUploadedFile(
                    BytesIO(image_data), None, 'patient_image.png', 'image/png', len(image_data), None
                )

            # Create and save the Patient object
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
                        patient_image=image_temp_file,
                        user=user
                    )

                    patient_group = Group.objects.get(pk=2)
                    patient_group.user_set.add(user)

                    patient.save()
                    messages.success(request, "Registration successful.")

            except Exception as e:
                messages.error(request, "Failed to save patient data.")
                print('a')
                return redirect('authen:register')

            del request.session['registration_data']
            del request.session['patient_image']
            return redirect('authen:login')

        elif 'cancel' in request.POST:
            return redirect('authen:register')
