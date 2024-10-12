from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from .forms import DoctorForm, AppointmentForm
from authen.models import Doctor
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from datetime import datetime, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
import json

class AppointTodayView(View):

    def get(self, request):
        department = request.GET.get('department', 'ทั้งหมด')
        current_time = datetime.now().time()
        #doctor_list = Doctor.objects.filter(start_time__lte=current_time, end_time__gte=current_time)
        doctor_list = Doctor.objects.all().order_by('id')

        if department and department != "ทั้งหมด":
            #doctor_list = Doctor.objects.filter(start_time__lte=current_time, end_time__gte=current_time, department__name=department)
            doctor_list = doctor_list.filter(department__name=department)

        today = date.today().strftime("%d/%m/%Y")
        today_day = date.today().strftime("%A")

        day_translation = {
            "Monday": "จันทร์",
            "Tuesday": "อังคาร",
            "Wednesday": "พุธ",
            "Thursday": "พฤหัส",
            "Friday": "ศุกร์",
            "Saturday": "เสาร์",
            "Sunday": "อาทิตย์"
        }

        today_day = day_translation.get(today_day)
        
        for doc in doctor_list:
            doc.start_time = doc.start_time.strftime("%H:%M")
            doc.end_time = doc.end_time.strftime("%H:%M")
        
            weekdays = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
            start_day, end_day = doc.shift_day.split('-')
            doc.day = []

            start_index = weekdays.index(start_day)
            end_index = weekdays.index(end_day)

            if start_index <= end_index:
                doc.day = weekdays[start_index:end_index + 1]
            else:
                doc.day = weekdays[start_index:] + weekdays[:end_index + 1]

        doctor_list_today = [doc for doc in doctor_list if today_day in doc.day]
    
        # ใช้ Paginator เพื่อแบ่งหน้า
        paginator = Paginator(doctor_list_today, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context ={
            'today': today,
            'today_day': today_day,
            'selected_department': department,
            'page_obj': page_obj
        }
        return render(request, 'appointment-today.html', context)
    
class DoctorListView(View):

    def get(self, request):
        department = request.GET.get('department', 'ทั้งหมด')  # ค่าเริ่มต้นเป็น 'ทั้งหมด'
        doctor_list = Doctor.objects.all().order_by('id')

        if department and department != "ทั้งหมด":
            doctor_list = doctor_list.filter(department__name=department)

        paginator = Paginator(doctor_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            "page_obj": page_obj,
            "selected_department": department  # เพิ่มตัวแปรนี้ใน context
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

    def get(self, request, doctor_id):
        # ดึงข้อมูลหมอจากฐานข้อมูล
        doc = Doctor.objects.get(pk=doctor_id)
        week = range(1, 8)

        # ลิสต์สำหรับวันแบบเต็มและแบบตัวย่อ
        weekdays_full = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weekdays_short = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]

        # แยกวันที่เริ่มต้นและสิ้นสุด
        start_day, end_day = doc.shift_day.split('-')

        # หาตำแหน่งของวันเริ่มต้นและสิ้นสุดจากลิสต์ full
        start_index = weekdays_full.index(start_day)
        end_index = weekdays_full.index(end_day)

        # สร้างลิสต์ใหม่ให้ doc.day เก็บวันเป็นตัวย่อ
        if start_index <= end_index:
            doc.day = weekdays_short[start_index:end_index + 1]
        else:
            doc.day = weekdays_short[start_index:] + weekdays_short[:end_index + 1]

        # Dictionary สำหรับแปลงตัวย่อภาษาอังกฤษเป็นตัวย่อภาษาไทย
        day_translation = {
            "Mon": "จ.",
            "Tue": "อ.",
            "Wed": "พ.",
            "Thu": "พฤ.",
            "Fri": "ศ.",
            "Sat": "ส.",
            "Sun": "อา."
        }

        # ค้นหาวันแรกที่หมอว่าง (เริ่มจากวันนี้)
        today = date.today()
        days_ahead = 0
        max_days_to_check = 7  # จำกัดการวนลูปภายใน 7 วันถัดไป
        default_start_date = None  # ค่าเริ่มต้น

        while days_ahead < max_days_to_check:
            day_eng = today.strftime("%a")  # ได้ตัวย่อภาษาอังกฤษ เช่น "Mon"
            day_short = day_translation.get(day_eng)  # แปลงเป็นตัวย่อภาษาไทย เช่น "จ."
            
            print(f"กำลังตรวจสอบวันที่: {today}, day_short: {day_short}")

            if day_short in doc.day:
                default_start_date = today.strftime("%d/%m/%Y")  # แปลงวันที่ให้เป็นรูปแบบ dd/mm/yyyy
                break
            today += timedelta(days=1)  # ถ้าหมอไม่ว่างในวันนี้ ให้เช็ควันถัดไป
            days_ahead += 1  # เพิ่มตัวนับจำนวนวันที่ตรวจสอบ

        if not default_start_date:
            # กรณีที่ไม่เจอวันว่างเลยใน 7 วันถัดไป
            default_start_date = date.today().strftime('%d/%m/%Y')  # ใช้วันที่ปัจจุบันแทน

        # เช็คหน้าก่อนว่ามาจากหน้าไหน
        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"
        
        form = AppointmentForm(initial={'appointment_date': default_start_date})

        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        updated_times = []

        # ใช้วันที่ปัจจุบันและเวลา 08:00
        current_time = datetime.combine(date.today(), datetime.strptime("08:00", "%H:%M").time())

        # ใช้วันที่ปัจจุบันและเวลา 18:00
        end_time = datetime.combine(date.today(), datetime.strptime("18:00", "%H:%M").time())

        # เวลาปัจจุบัน (รวมวันที่และเวลา)
        now = datetime.now()

        # ช่วงเวลาเข้าเวร
        start_bound = datetime.combine(date.today(), doc.start_time)
        end_bound = datetime.combine(date.today(), doc.end_time)

        # วนลูปเพื่อคำนวณช่วงเวลา
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")

            # ตรวจสอบว่าเวลาปัจจุบันน้อยกว่าเวลาที่กำหนดไว้ (now)
            if current_time < now:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))
            elif start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time

        # แปลง doc.day เป็น JSON เพื่อใช้ใน JavaScript
        doc_days_json = mark_safe(json.dumps(doc.day))

        # ส่งข้อมูลไปยัง template
        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            'form': form,  # ฟอร์มนัดหมาย
            'previous': previous,  # หน้าที่มาก่อน
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'default_start_date': default_start_date,  # ส่งวันที่ที่หมอว่างวันแรกไปยัง template
        }

        return render(request, 'appointment.html', context)
    def post(self, request, doctor_id):
        form = AppointmentForm(request.POST, request.FILES)
        
        doc = Doctor.objects.get(pk=doctor_id)
        today = date.today().strftime('%d/%m/%Y')
        week = range(1,8)
        today_day = date.today().strftime("%A")

        day_translation = {
            "Monday": "จันทร์",
            "Tuesday": "อังคาร",
            "Wednesday": "พุธ",
            "Thursday": "พฤหัส",
            "Friday": "ศุกร์",
            "Saturday": "เสาร์",
            "Sunday": "อาทิตย์"
        }

        today_day = day_translation.get(today_day)
        print(today_day)
        
        doc.start_time = doc.start_time.strftime("%H:%M")
        doc.end_time = doc.end_time.strftime("%H:%M")
    
        weekdays = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        start_day, end_day = doc.shift_day.split('-')
        doc.day = []

        start_index = weekdays.index(start_day)
        end_index = weekdays.index(end_day)

        if start_index <= end_index:
            doc.day = weekdays[start_index:end_index + 1]
        else:
            doc.day = weekdays[start_index:] + weekdays[:end_index + 1]

        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"

        form = AppointmentForm()

        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        times = []
        current_time = datetime.strptime("08:00", "%H:%M")
        end_time = datetime.strptime("18:00", "%H:%M")

        if isinstance(doc.start_time, str):
            start_time_obj = datetime.strptime(doc.start_time, "%H:%M").time()
        else:
            start_time_obj = doc.start_time

        if isinstance(doc.end_time, str):
            end_time_obj = datetime.strptime(doc.end_time, "%H:%M").time()
        else:
            end_time_obj = doc.end_time

        # ดึง hour และ minute จาก start_time_obj และ end_time_obj
        start_hour = start_time_obj.hour
        start_minute = start_time_obj.minute
        end_hour = end_time_obj.hour
        end_minute = end_time_obj.minute

        # ใช้ replace เพื่อแทนค่าของ hour และ minute ใน current_time
        start_bound = current_time.replace(hour=start_hour, minute=start_minute)
        end_bound = current_time.replace(hour=end_hour, minute=end_minute)

        # สร้างลิสต์ของช่วงเวลาพร้อมกับตรวจสอบว่าอยู่ในช่วงเวลาที่กำหนดหรือไม่
        updated_times = []
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")

            # ตรวจสอบว่าช่วงเวลานี้อยู่ในช่วง start_bound และ end_bound หรือไม่
            if start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time
                

        context = {
            'doc': doc,
            'week': week,       
            'start': doc.start_time,
            'end': doc.end_time,
            'today': today,
            'times': times,  # ส่งค่า times ไปยัง template,
            'form': form,
            'previous': previous,
            'today': today,
            'today_day': today_day,
            'updated_times' : updated_times
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

    def get(self, request):
        doc = Doctor.objects.get(pk=request.user.doctor.id)
        today = date.today().strftime('%d/%m/%Y')
        week = range(1,8)
        today_day = date.today().strftime("%A")

        day_translation = {
            "Monday": "จันทร์",
            "Tuesday": "อังคาร",
            "Wednesday": "พุธ",
            "Thursday": "พฤหัส",
            "Friday": "ศุกร์",
            "Saturday": "เสาร์",
            "Sunday": "อาทิตย์"
        }

        today_day = day_translation.get(today_day)
        print(today_day)
        
        doc.start_time = doc.start_time.strftime("%H:%M")
        doc.end_time = doc.end_time.strftime("%H:%M")
    
        weekdays = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        start_day, end_day = doc.shift_day.split('-')
        doc.day = []

        start_index = weekdays.index(start_day)
        end_index = weekdays.index(end_day)

        if start_index <= end_index:
            doc.day = weekdays[start_index:end_index + 1]
        else:
            doc.day = weekdays[start_index:] + weekdays[:end_index + 1]

        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"

        form = AppointmentForm()

        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        times = []
        current_time = datetime.strptime("08:00", "%H:%M")
        end_time = datetime.strptime("18:00", "%H:%M")

        if isinstance(doc.start_time, str):
            start_time_obj = datetime.strptime(doc.start_time, "%H:%M").time()
        else:
            start_time_obj = doc.start_time

        if isinstance(doc.end_time, str):
            end_time_obj = datetime.strptime(doc.end_time, "%H:%M").time()
        else:
            end_time_obj = doc.end_time

        # ดึง hour และ minute จาก start_time_obj และ end_time_obj
        start_hour = start_time_obj.hour
        start_minute = start_time_obj.minute
        end_hour = end_time_obj.hour
        end_minute = end_time_obj.minute

        # ใช้ replace เพื่อแทนค่าของ hour และ minute ใน current_time
        start_bound = current_time.replace(hour=start_hour, minute=start_minute)
        end_bound = current_time.replace(hour=end_hour, minute=end_minute)

        # สร้างลิสต์ของช่วงเวลาพร้อมกับตรวจสอบว่าอยู่ในช่วงเวลาที่กำหนดหรือไม่
        updated_times = []
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")

            # ตรวจสอบว่าช่วงเวลานี้อยู่ในช่วง start_bound และ end_bound หรือไม่
            if start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time
                

        context = {
            'doc': doc,
            'week': week,       
            'start': doc.start_time,
            'end': doc.end_time,
            'today': today,
            'times': times,  # ส่งค่า times ไปยัง template,
            'form': form,
            'previous': previous,
            'today': today,
            'today_day': today_day,
            'updated_times' : updated_times
        }
        return render(request, 'doc_appointment.html', context)