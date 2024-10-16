from django.shortcuts import render, redirect
from django.views import View
from .forms import DoctorForm, AppointmentForm, AppointmentEditForm
from authen.models import Doctor, Patient
from appoint.models import Appointment
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
import json
from django.http import JsonResponse


# function
def day(date, format):

    if (format == "full"):
        today_day = date.strftime("%A")

        day_translation = {
            "Monday": "จันทร์",
            "Tuesday": "อังคาร",
            "Wednesday": "พุธ",
            "Thursday": "พฤหัส",
            "Friday": "ศุกร์",
            "Saturday": "เสาร์",
            "Sunday": "อาทิตย์"
        }
    elif (format == "short"):
        today_day = date.strftime("%a")

        day_translation = {
            "Mon": "จ.",
            "Tue": "อ.",
            "Wed": "พ.",
            "Thu": "พฤ.",
            "Fri": "ศ.",
            "Sat": "ส.",
            "Sun": "อา."
        }

    today_day = day_translation.get(today_day)

    return today_day


def doc_shift(doc, today_day, format):
    weekdays = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
    weekdays_short = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]
    start_day, end_day = doc.shift_day.split('-')
    doc.day = []

    start_index = weekdays.index(start_day)
    end_index = weekdays.index(end_day)

    if format == "full":
        if start_index <= end_index:
            doc.day = weekdays[start_index:end_index + 1]
        else:
            doc.day = weekdays[start_index:] + weekdays[:end_index + 1]

    elif format == "short":
        if start_index <= end_index:
            doc.day = weekdays_short[start_index:end_index + 1]
        else:
            doc.day = weekdays_short[start_index:] + weekdays_short[:end_index + 1]

    return doc.day


def paginator(request, list, num):
    paginator = Paginator(list, num)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return page_obj 

def beforeAppoint(request):
    referrer = request.META.get('HTTP_REFERER')
    previous = ""
    if referrer:
        if "appointment" in referrer:
            previous = "คิวพบแพทย์"
        elif "doctor-list" in referrer:
            previous = "รายชื่อแพทย์"

    return previous

def doc_Schedule(appointment_date, appointment_day, doc, today, appoint_time):
    min = 10
    updated_times = []
    current_time = datetime.combine(appointment_date, datetime.strptime("08:00", "%H:%M").time())
    end_time = datetime.combine(appointment_date, datetime.strptime("18:00", "%H:%M").time())

    start_bound = datetime.combine(appointment_date, doc.start_time)
    end_bound = datetime.combine(appointment_date, doc.end_time)

    while current_time < end_time:
        start_time_str = current_time.strftime("%H:%M")
        next_time = current_time + timedelta(minutes=min)
        end_time_str = next_time.strftime("%H:%M")
        
        if appointment_day in doc.day:

            if (appointment_date.date() == today.date()):
                if current_time < today:
                    updated_times.append((start_time_str, end_time_str, "out_of_range"))
                elif start_time_str in appoint_time :
                    updated_times.append((start_time_str, end_time_str, "appointment"))
                elif start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                    updated_times.append((start_time_str, end_time_str, "in_range"))
                else:
                    updated_times.append((start_time_str, end_time_str, "out_of_range"))
            elif (appointment_date.date() < today.date()):
                updated_times.append((start_time_str, end_time_str, "out_of_range"))
            else:
                if start_time_str in appoint_time :
                    updated_times.append((start_time_str, end_time_str, "appointment"))
                else:
                    updated_times.append((start_time_str, end_time_str, "in_range"))
        else:
            updated_times.append((start_time_str, end_time_str, "out_of_range"))
        current_time = next_time

    return updated_times

def doc_appoint(doc, appointment_date):
    appointments = Appointment.objects.filter(doctor=doc, appointment_date=appointment_date)
    appoint_time = [
        appointment_time.strftime('%H:%M') for appointment_time in appointments.values_list('appointment_time', flat=True)
    ]

    return appoint_time

class AppointTodayView(View):

    def get(self, request):
        department = request.GET.get('department', 'ทั้งหมด')

        current = datetime.now()
        current_time = current.time()
        current_date = current.strftime('%Y-%m-%d')
        today = current.date().strftime("%d/%m/%Y")

        doctor_list = Doctor.objects.filter(start_time__lte=current_time, end_time__gte=current_time)
        if department and department != "ทั้งหมด":
            doctor_list = Doctor.objects.filter(start_time__lte=current_time, end_time__gte=current_time, department__name=department)

        today_day = day(current.date(), "full")
        for doc in doctor_list:
            doc.start_time = doc.start_time.strftime("%H:%M")
            doc.end_time = doc.end_time.strftime("%H:%M")
            doc.day = doc_shift(doc, today_day, "full")
        doctor_list_today = [doc for doc in doctor_list if today_day in doc.day]
        
        page_obj = paginator(request, doctor_list_today, 6)

        context ={
            'today': today,
            'today_day': today_day,
            'selected_department': department,
            'page_obj': page_obj,
            'current_date' :current_date
        }
        return render(request, 'appointment-today.html', context)
    
class DoctorListView(View):

    def get(self, request):
        current = datetime.now()
        current_date = current.strftime('%Y-%m-%d')

        department = request.GET.get('department', 'ทั้งหมด')
        doctor_list = Doctor.objects.all().order_by('id')

        if department and department != "ทั้งหมด":
            doctor_list = doctor_list.filter(department__name=department)

        page_obj = paginator(request, doctor_list, 6)
        
        context = {
            "page_obj": page_obj,
            "selected_department": department,
            'current_date': current_date
        }
        return render(request, 'doctor-list.html', context)
    

class CreateDoctorView(View):

    def get(self, request):
        form = DoctorForm()
        context={
            "form": form,
        }
        return render(request, 'create_doctor.html', context)
    
    def post(self, request):
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                with transaction.atomic():
                    doc = form.save(commit=False)
                    User.objects.create_user(
                            username= form.cleaned_data["personalID"],
                            password="Xy7#p9Tk!",
                            first_name= form.cleaned_data["first_name"],
                            last_name= form.cleaned_data["last_name"],
                            email= form.cleaned_data["email"]
                        )
                    
                    user = authenticate(
                        request,
                        username= form.cleaned_data["personalID"],
                        password="Xy7#p9Tk!"
                    )

                    doctor_group = Group.objects.get(name='doctor')
                    user.groups.add(doctor_group)
                    
                    doc.user = user
                    doc.save()

            except ObjectDoesNotExist:
                print("ไม่มีบัญชีหมอคนนี้")
            return redirect('appoint:doctor-list')

        return render(request, "create_doctor.html", {
            "form": form
        })
    
class AppointmentView(LoginRequiredMixin,View):
    login_url = "/hopelife/login/"
    
    def get(self, request, doctor_id, current_date):
        doc = Doctor.objects.get(pk=doctor_id)
        week = range(1, 8)

        today = datetime.now()
        today_day = day(today, "full")
        
        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")
        appointment_day = day(appointment_date, "short")
        appoint_time = doc_appoint(doc.user, appointment_date)

        doc.day = doc_shift(doc, today_day, "short")

        previous = beforeAppoint(request)
        
        form = AppointmentForm(initial={'appointment_date': appointment_date_str})

        updated_times = doc_Schedule(appointment_date, appointment_day, doc, today, appoint_time)

        doc_days_json = mark_safe(json.dumps(doc.day))


        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            'form': form,  # ฟอร์มนัดหมาย
            'previous': previous,  # หน้าที่มาก่อน
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'today_day' : today_day,
            'appointment_date_str': appointment_date_str,
            'current_date': current_date
        }

        return render(request, 'appointment.html', context)
    

    def post(self, request, doctor_id, current_date):
        form = AppointmentForm(request.POST, request.FILES)

        doc = Doctor.objects.get(pk=doctor_id)
        week = range(1, 8)

        today = datetime.now()
        today_day = day(today, "full")
        
        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")
        appointment_day = day(appointment_date, "short")
        appoint_time = doc_appoint(doc.user, appointment_date)

        doc.day = doc_shift(doc, today_day, "short")

        previous = beforeAppoint(request)

        updated_times = doc_Schedule(appointment_date, appointment_day, doc, today, appoint_time)

        doc_days_json = mark_safe(json.dumps(doc.day))


        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            'form': form,  # ฟอร์มนัดหมาย
            'previous': previous,  # หน้าที่มาก่อน
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'today_day' : today_day,
            'appointment_date_str': appointment_date_str,
            'current_date': current_date
        }
        
        
        if form.is_valid():
            app = form.save(commit=False)
            app.patient = request.user
            app.doctor = doc.user
            app.save()
            return redirect('appoint:appoint-today')

        return render(request, 'appointment.html', context)


class DoctorAppointmentView(LoginRequiredMixin,View):
    login_url = "/hopelife/login/"

    def get(self, request, current_date):
        doc = Doctor.objects.get(user=request.user)
        week = range(1, 8)

        today = datetime.now()
        today_day = day(today, "full")

        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")
        appointment_day = day(appointment_date, "short")
        appoint_time = doc_appoint(request.user, appointment_date)

        doc.day = doc_shift(doc, today_day, "short")

        updated_times = doc_Schedule(appointment_date, appointment_day, doc, today, appoint_time)

        doc_days_json = mark_safe(json.dumps(doc.day))

        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'today_day' : today_day,
            'appointment_date_str': appointment_date_str,
        }

        return render(request, 'doc_appointment.html', context)

    def post(self, request, current_date):
        appointment_time = request.POST.get('appointment_time')
        print(f"เวลานัดหมายที่เลือกคือ: {appointment_time}")

        return redirect('appoint:doc_appointment_edit', current_date=current_date, appointment_time=appointment_time)

class DoctorAppointmentEditView(LoginRequiredMixin,View):
    def get(self, request, current_date, appointment_time):
        app = Appointment.objects.get(appointment_date=current_date, doctor=request.user, appointment_time=appointment_time)
        app_patient = Patient.objects.get(user=app.patient)


        doc = Doctor.objects.get(user=request.user)
        week = range(1, 8)

        today = datetime.now()
        today_day = day(today, "full")

        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")
        appointment_day = day(appointment_date, "short")
        appoint_time = doc_appoint(request.user, appointment_date)

        doc.day = doc_shift(doc, today_day, "short")

        updated_times = doc_Schedule(appointment_date, appointment_day, doc, today, appoint_time)
    
        initial_data = {
            'appointment_time': app.appointment_time.strftime("%H:%M")
        }
    
        form = AppointmentEditForm(instance=app, initial=initial_data)
        doc_days_json = mark_safe(json.dumps(doc.day))

        # ส่งข้อมูลไปยัง template
        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'today_day' : today_day,
            'appointment_date_str': appointment_date_str,
            'app': app,
            'app_patient':app_patient,
            'current_date':current_date,
            'form': form,
            'appointment_time': appointment_time
        }

        if form.is_valid():
            form.save()
            return redirect('appoint:doc_appointment' ,current_date=current_date)

        return render(request, 'doc_appointment_edit.html', context)
    
    def post(self, request, current_date, appointment_time):
        app = Appointment.objects.get(appointment_date=current_date, doctor=request.user, appointment_time=appointment_time)
        app_patient = Patient.objects.get(user=app.patient)


        doc = Doctor.objects.get(user=request.user)
        week = range(1, 8)

        today = datetime.now()
        today_day = day(today, "full")

        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")
        appointment_day = day(appointment_date, "short")
        appoint_time = doc_appoint(request.user, appointment_date)

        doc.day = doc_shift(doc, today_day, "short")

        updated_times = doc_Schedule(appointment_date, appointment_day, doc, today, appoint_time)
    
        form = AppointmentEditForm(request.POST, instance=app)
        doc_days_json = mark_safe(json.dumps(doc.day))

        # ส่งข้อมูลไปยัง template
        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'today_day' : today_day,
            'today_day' : today_day,
            'appointment_date_str': appointment_date_str,
            'app': app,
            'app_patient':app_patient,
            'current_date':current_date,
            'form': form,
            'appointment_time': appointment_time
        }

        if form.is_valid():
            try:
                with transaction.atomic():
                    app = form.save(commit=False)
                    appointment_time = form.cleaned_data["appointment_time"]

                    # ตรวจสอบว่า appointment_time อยู่ใน appoint_time หรือไม่
                    if appointment_time in appoint_time:
                        form.add_error('appointment_time', 'มีนัดแล้วในเวลานี้ กรุณาเลือกเวลาอื่น')
                        return render(request, 'doc_appointment_edit.html', context)
                    else:
                        print("update appointment")
                        app.save()
                        return redirect('appoint:doc_appointment', current_date=current_date)

            except ObjectDoesNotExist:
                print("ไม่มีสามารถแก้ไขนัดหมายได้")

        return render(request, 'doc_appointment_edit.html', context)
    
    def delete(self, request, current_date, appointment_time):
        try:
            app = Appointment.objects.get(appointment_date=current_date, doctor=request.user, appointment_time=appointment_time)
            app.delete()  # Delete the appointment
            return JsonResponse({'message': 'Appointment deleted successfully'}, status=200)
        except Appointment.DoesNotExist:
            return JsonResponse({'error': 'Appointment not found'}, status=404)
        # app = Appointment.objects.get(appointment_date=current_date, doctor=request.user, appointment_time=appointment_time)
        # app.delete()

        # return JsonResponse({'foo':'bar'}, status=200)