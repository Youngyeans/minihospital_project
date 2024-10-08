import json
from decimal import Decimal
from django.shortcuts import render, redirect
from django.views import View
from .models import Patient
from .forms import PatientRegistrationForm
from django.contrib import messages
from datetime import datetime

class LoginView(View):
    def get(self, request):
        form = PatientRegistrationForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If user is valid, log them in and redirect to home
            login(request, user)
            return redirect('home')  # Change to your home URL name
        else:
            # Show error message
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html', {"form": PatientRegistrationForm()})

class LogoutView(View):
    def get(self, request):
        pass

class RegisterView(View):
    def get(self, request):
        referrer = request.META.get('HTTP_REFERER')
        if referrer:
            if "validation" in referrer:
                registration_data_json = request.session.get('registration_data', {})
                registration_data = json.loads(registration_data_json)
                form = PatientRegistrationForm(initial=registration_data) 
            else:
                form = PatientRegistrationForm()
            return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = PatientRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Prepare data without saving to the database yet
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
                'height': str(form.cleaned_data['height']),  # Convert Decimal to string
                'weight': str(form.cleaned_data['weight']),  # Convert Decimal to string
                'blood_group': form.cleaned_data['blood_group'],
                'allergy': form.cleaned_data['allergy'],
                'address': form.cleaned_data['address'],
                'patient_image': request.FILES.get('patient_image', None),  # Include image if uploaded
            }
            # Convert to JSON
            json_data = json.dumps(context)
            request.session['registration_data'] = json_data  # Save JSON string to session
            return redirect('authen:validation')
        
        return render(request, 'register.html', {'form': form})

class ValidationView(View):
    def get(self, request):
        # Retrieve the JSON data from the session
        registration_data_json = request.session.get('registration_data', None)
        if registration_data_json is None:
            messages.error(request, "No registration data found.")
            return redirect('authen:register')  # Redirect back to the register page if no data found

        # Convert JSON string back to Python dictionary
        registration_data = json.loads(registration_data_json)
        return render(request, 'validation.html', registration_data)

    def post(self, request):
        print("Post method triggered")  # Debugging line
        if 'save' in request.POST:
            print("Save button clicked")  # Debugging line

            # Retrieve the JSON data from the session
            registration_data_json = request.session.get('registration_data', None)
            if registration_data_json is None:
                messages.error(request, "No registration data found.")
                return redirect('authen:register')

            registration_data = json.loads(registration_data_json)  # Convert JSON back to dictionary
            
            # Create a new Patient object and save to the database
            try:
                patient = Patient(
                    prefix=registration_data['prefix'],
                    first_name=registration_data['first_name'],
                    last_name=registration_data['last_name'],
                    personalID=registration_data['personalID'],
                    nationality=registration_data['nationality'],
                    phone=registration_data['phone'],
                    gender=registration_data['gender'],
                    DOB=datetime.strptime(registration_data['DOB'], '%Y-%m-%d').date(),
                    height=Decimal(registration_data['height']),
                    weight=Decimal(registration_data['weight']),
                    blood_group=registration_data['blood_group'],
                    allergy=registration_data['allergy'],
                    address=registration_data['address'],
                    patient_image=registration_data.get('patient_image'),
                )
                patient.save()  # Save the patient data to the database
                messages.success(request, "Registration successful.")
                del request.session['registration_data']  # Clear session data after saving
                return redirect('authen:login')
            except Exception as e:
                print(f"Error saving patient: {e}")  # Debugging line
                messages.error(request, "Failed to save patient data.")

        elif 'cancel' in request.POST:
            print("Cancel button clicked")  # Debugging line
            # del request.session['registration_data']
            return redirect('authen:register')
