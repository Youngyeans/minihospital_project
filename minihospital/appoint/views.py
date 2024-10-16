from django.shortcuts import render, redirect
from django.views import View
from datetime import date
from .forms import DoctorForm, AppointmentForm
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

class AppointTodayView(View):

    def get(self, request):
        department = request.GET.get('department', 'ทั้งหมด')
        current = datetime.now()
        #current = datetime(2024, 10, 16, 9, 30)
        current_time = current.time()
        current_date = current.strftime('%Y-%m-%d')
        doctor_list = Doctor.objects.filter(start_time__lte=current_time, end_time__gte=current_time)
        # doctor_list = Doctor.objects.all().order_by('id')

        if department and department != "ทั้งหมด":
            doctor_list = Doctor.objects.filter(start_time__lte=current_time, end_time__gte=current_time, department__name=department)
            # doctor_list = doctor_list.filter(department__name=department)

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
            'page_obj': page_obj,
            'current_date' :current_date
        }
        return render(request, 'appointment-today.html', context)
    
class DoctorListView(View):

    def get(self, request):
        current = datetime(2024, 10, 16, 9, 30)
        current_date = current.strftime('%Y-%m-%d')
        department = request.GET.get('department', 'ทั้งหมด')  # ค่าเริ่มต้นเป็น 'ทั้งหมด'
        doctor_list = Doctor.objects.all().order_by('id')

        if department and department != "ทั้งหมด":
            doctor_list = doctor_list.filter(department__name=department)

        paginator = Paginator(doctor_list, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
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
        # ดึงข้อมูลหมอจากฐานข้อมูล
        doc = Doctor.objects.get(pk=doctor_id)
        week = range(1, 8)
        # today = datetime.now()
        today = datetime(2024, 10, 16, 9, 30)
        
        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")




        # หาว่าวันนี้คือวันอะไร เอาไปเทียบกับ doc.day เพื่อดูว่าหมอคนที่อยู่ในเวรมั้ย
        appointment_day = appointment_date.strftime("%a")
        today_day = today.strftime("%A")
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



        # หาเป็นวันที่หมอคนนี้จะเริ่มทำงาน
        day_translation = {
            "Mon": "จ.",
            "Tue": "อ.",
            "Wed": "พ.",
            "Thu": "พฤ.",
            "Fri": "ศ.",
            "Sat": "ส.",
            "Sun": "อา."
        }

        appointment_day = day_translation.get(appointment_day)

        #หาช่วงวันที่หมอทำงาน 
        weekdays_full = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weekdays_short = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]
        start_day, end_day = doc.shift_day.split('-') #แยกวันที่เริ่มเวร, วันสุดท้ายของเวรใน 1 สัปดาห์
        start_index = weekdays_full.index(start_day)
        end_index = weekdays_full.index(end_day)
        # สร้างลิสต์เก็บวันเป็นตัวย่อ
        if start_index <= end_index:
            doc.day = weekdays_short[start_index:end_index + 1]
        else:
            doc.day = weekdays_short[start_index:] + weekdays_short[:end_index + 1]
        print(f"doc.day= {doc.day}")




        today_date = today.date()
        days_ahead = 0
        max_days_to_check = 7  # ภายใน 1 สัปดาห์
        default_start_date = None  # ค่าเริ่มต้น

        while days_ahead < max_days_to_check:
            day_eng = today_date.strftime("%a")  
            day_short = day_translation.get(day_eng)
            
            print(f"กำลังตรวจสอบวันที่: {today_date}, day_short: {day_short}")

            if day_short in doc.day:
                default_start_date = today_date.strftime("%d/%m/%Y")  # แปลงวันที่ให้เป็นรูปแบบ dd/mm/yyyy
                break
            today_date += timedelta(days=1)  # ถ้าหมอไม่ว่างในวันนี้ ให้เช็ควันถัดไป
            days_ahead += 1  # เพิ่มตัวนับจำนวนวันที่ตรวจสอบ

        if not default_start_date:
            # กรณีที่ไม่เจอวันว่างเลยใน 7 วันถัดไป
            default_start_date = today.strftime('%d/%m/%Y')  # ใช้วันที่ปัจจุบันแทน

        # เช็คหน้าก่อนว่ามาจากหน้าไหน
        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"
        


        form = AppointmentForm(initial={'appointment_date': appointment_date.strftime('%d/%m/%Y')})




        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        updated_times = []

        # ใช้วันที่ปัจจุบันและเวลา 08:00
        current_time = datetime.combine(appointment_date, datetime.strptime("08:00", "%H:%M").time())

        # ใช้วันที่ปัจจุบันและเวลา 18:00
        end_time = datetime.combine(appointment_date, datetime.strptime("18:00", "%H:%M").time())

        # เวลาปัจจุบัน (รวมวันที่และเวลา)
        # appointment_date = request.POST.get('appointment_date')
        # if appointment_date is None:
        #     appointment_date = default_start_date

        # print(f"appointment_date:{appointment_date}, today_date: {today_date.strftime("%d/%m/%Y")}")

        # ช่วงเวลาเข้าเวร
        start_bound = datetime.combine(appointment_date, doc.start_time)
        end_bound = datetime.combine(appointment_date, doc.end_time)


        # if appointment_date == today_date.strftime("%d/%m/%Y"):
        #     print(f"today")
        # else:
        #     print(f"not today")

        print(f"appointment_date: {appointment_date}, default_start_date : {default_start_date}")
        print(f"appointment_day: {appointment_day}")
        # วนลูปเพื่อคำนวณช่วงเวลา
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")
            
            if appointment_day in doc.day:
                if (appointment_date == datetime.strptime(default_start_date, '%d/%m/%Y')):
                    # ตรวจสอบว่าเวลาปัจจุบันน้อยกว่าเวลาที่กำหนดไว้ (now)
                    if current_time < today:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                    elif start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                        updated_times.append((start_time_str, end_time_str, "in_range"))
                    else:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                else:
                    updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time

        # แปลง doc.day เป็น JSON เพื่อใช้ใน JavaScript
        doc_days_json = mark_safe(json.dumps(doc.day))
        # print(f"updated_times: {updated_times}")

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
            'default_start_date': default_start_date,  # ส่งวันที่ที่หมอว่างวันแรกไปยัง template,
            'today_day' : today_day,
            'today_date': today_date.strftime("%d/%m/%Y"),
            'appointment_date_str': appointment_date_str,
            'current_date': current_date
        }

        return render(request, 'appointment.html', context)
    


    def post(self, request, doctor_id, current_date):
        form = AppointmentForm(request.POST, request.FILES)

        # ดึงข้อมูลหมอจากฐานข้อมูล
        doc = Doctor.objects.get(pk=doctor_id)
        week = range(1, 8)
        today = datetime.now()
        # today = datetime(2024, 10, 16, 9, 30)
        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')




        # หาว่าวันนี้คือวันอะไร เอาไปเทียบกับ doc.day เพื่อดูว่าหมอคนที่อยู่ในเวรมั้ย
        appointment_day = appointment_date.strftime("%a")
        today_day = today.strftime("%A")
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



        # หาเป็นวันที่หมอคนนี้จะเริ่มทำงาน
        day_translation = {
            "Mon": "จ.",
            "Tue": "อ.",
            "Wed": "พ.",
            "Thu": "พฤ.",
            "Fri": "ศ.",
            "Sat": "ส.",
            "Sun": "อา."
        }

        appointment_day = day_translation.get(appointment_day)

        #หาช่วงวันที่หมอทำงาน 
        weekdays_full = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weekdays_short = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]
        start_day, end_day = doc.shift_day.split('-') #แยกวันที่เริ่มเวร, วันสุดท้ายของเวรใน 1 สัปดาห์
        start_index = weekdays_full.index(start_day)
        end_index = weekdays_full.index(end_day)
        # สร้างลิสต์เก็บวันเป็นตัวย่อ
        if start_index <= end_index:
            doc.day = weekdays_short[start_index:end_index + 1]
        else:
            doc.day = weekdays_short[start_index:] + weekdays_short[:end_index + 1]
        print(f"doc.day= {doc.day}")




        today_date = today.date()
        days_ahead = 0
        max_days_to_check = 7  # ภายใน 1 สัปดาห์
        default_start_date = None  # ค่าเริ่มต้น

        while days_ahead < max_days_to_check:
            day_eng = today_date.strftime("%a")  
            day_short = day_translation.get(day_eng)
            
            print(f"กำลังตรวจสอบวันที่: {today_date}, day_short: {day_short}")

            if day_short in doc.day:
                default_start_date = today_date.strftime("%d/%m/%Y")  # แปลงวันที่ให้เป็นรูปแบบ dd/mm/yyyy
                break
            today_date += timedelta(days=1)  # ถ้าหมอไม่ว่างในวันนี้ ให้เช็ควันถัดไป
            days_ahead += 1  # เพิ่มตัวนับจำนวนวันที่ตรวจสอบ

        if not default_start_date:
            # กรณีที่ไม่เจอวันว่างเลยใน 7 วันถัดไป
            default_start_date = today.strftime('%d/%m/%Y')  # ใช้วันที่ปัจจุบันแทน

        # เช็คหน้าก่อนว่ามาจากหน้าไหน
        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"
        






        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        updated_times = []

        # ใช้วันที่ปัจจุบันและเวลา 08:00
        current_time = datetime.combine(appointment_date, datetime.strptime("08:00", "%H:%M").time())

        # ใช้วันที่ปัจจุบันและเวลา 18:00
        end_time = datetime.combine(appointment_date, datetime.strptime("18:00", "%H:%M").time())

        # เวลาปัจจุบัน (รวมวันที่และเวลา)
        # appointment_date = request.POST.get('appointment_date')
        # if appointment_date is None:
        #     appointment_date = default_start_date

        # print(f"appointment_date:{appointment_date}, today_date: {today_date.strftime("%d/%m/%Y")}")

        # ช่วงเวลาเข้าเวร
        start_bound = datetime.combine(appointment_date, doc.start_time)
        end_bound = datetime.combine(appointment_date, doc.end_time)


        # if appointment_date == today_date.strftime("%d/%m/%Y"):
        #     print(f"today")
        # else:
        #     print(f"not today")

        print(f"appointment_date: {appointment_date}, default_start_date : {default_start_date}")
        print(f"appointment_day: {appointment_day}")
        # วนลูปเพื่อคำนวณช่วงเวลา
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")
            
            if appointment_day in doc.day:
                if (appointment_date == datetime.strptime(default_start_date, '%d/%m/%Y')):
                    # ตรวจสอบว่าเวลาปัจจุบันน้อยกว่าเวลาที่กำหนดไว้ (now)
                    if current_time < today:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                    elif start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                        updated_times.append((start_time_str, end_time_str, "in_range"))
                    else:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                else:
                    updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time

        # แปลง doc.day เป็น JSON เพื่อใช้ใน JavaScript
        doc_days_json = mark_safe(json.dumps(doc.day))
        print(f"updated_times: {updated_times}")

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
            'default_start_date': default_start_date,  # ส่งวันที่ที่หมอว่างวันแรกไปยัง template,
            'today_day' : today_day,
            'today_date': today_date.strftime("%d/%m/%Y"),
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
        print(f"ค่าวันที่ส่งมาคือ: {current_date}")
        print("--------------------------------------------------------")
        # form = AppointmentForm(instance=project)
        # if form.is_valid():                                                                      
        #     form.save()                                                                          
        #     return redirect('appoint:doc_appointment')
        # ดึงข้อมูลหมอจากฐานข้อมูล
        doc = Doctor.objects.get(user=request.user)
        week = range(1, 8)
        today = datetime.now()
        # today = datetime(2024, 10, 16, 9, 30)
        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")

        # Query ที่กรองตาม doctor และวันที่นัดหมาย
        appointments = Appointment.objects.filter(doctor=request.user, appointment_date=appointment_date)

        # ดึงฟิลด์ appointment_time และแปลงเวลาให้อยู่ในรูป %H:%M
        appoint_time = [
            appointment_time.strftime('%H:%M') for appointment_time in appointments.values_list('appointment_time', flat=True)
        ]

        # หาว่าวันนี้คือวันอะไร เอาไปเทียบกับ doc.day เพื่อดูว่าหมอคนที่อยู่ในเวรมั้ย
        appointment_day = appointment_date.strftime("%a")
        today_day = today.strftime("%A")
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



        # หาเป็นวันที่หมอคนนี้จะเริ่มทำงาน
        day_translation = {
            "Mon": "จ.",
            "Tue": "อ.",
            "Wed": "พ.",
            "Thu": "พฤ.",
            "Fri": "ศ.",
            "Sat": "ส.",
            "Sun": "อา."
        }

        appointment_day = day_translation.get(appointment_day)

        #หาช่วงวันที่หมอทำงาน 
        weekdays_full = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weekdays_short = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]
        start_day, end_day = doc.shift_day.split('-') #แยกวันที่เริ่มเวร, วันสุดท้ายของเวรใน 1 สัปดาห์
        start_index = weekdays_full.index(start_day)
        end_index = weekdays_full.index(end_day)
        # สร้างลิสต์เก็บวันเป็นตัวย่อ
        if start_index <= end_index:
            doc.day = weekdays_short[start_index:end_index + 1]
        else:
            doc.day = weekdays_short[start_index:] + weekdays_short[:end_index + 1]
        print(f"doc.day= {doc.day}")




        today_date = today.date()
        days_ahead = 0
        max_days_to_check = 7  # ภายใน 1 สัปดาห์
        default_start_date = None  # ค่าเริ่มต้น

        while days_ahead < max_days_to_check:
            day_eng = today_date.strftime("%a")  
            day_short = day_translation.get(day_eng)
            
            print(f"กำลังตรวจสอบวันที่: {today_date}, day_short: {day_short}")

            if day_short in doc.day:
                default_start_date = today_date.strftime("%d/%m/%Y")  # แปลงวันที่ให้เป็นรูปแบบ dd/mm/yyyy
                break
            today_date += timedelta(days=1)  # ถ้าหมอไม่ว่างในวันนี้ ให้เช็ควันถัดไป
            days_ahead += 1  # เพิ่มตัวนับจำนวนวันที่ตรวจสอบ

        if not default_start_date:
            # กรณีที่ไม่เจอวันว่างเลยใน 7 วันถัดไป
            default_start_date = today.strftime('%d/%m/%Y')  # ใช้วันที่ปัจจุบันแทน

        # เช็คหน้าก่อนว่ามาจากหน้าไหน
        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"
        





        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        updated_times = []

        # ใช้วันที่ปัจจุบันและเวลา 08:00
        current_time = datetime.combine(appointment_date, datetime.strptime("08:00", "%H:%M").time())

        # ใช้วันที่ปัจจุบันและเวลา 18:00
        end_time = datetime.combine(appointment_date, datetime.strptime("18:00", "%H:%M").time())

        # เวลาปัจจุบัน (รวมวันที่และเวลา)
        # appointment_date = request.POST.get('appointment_date')
        # if appointment_date is None:
        #     appointment_date = default_start_date

        # print(f"appointment_date:{appointment_date}, today_date: {today_date.strftime("%d/%m/%Y")}")

        # ช่วงเวลาเข้าเวร
        start_bound = datetime.combine(appointment_date, doc.start_time)
        end_bound = datetime.combine(appointment_date, doc.end_time)


        # if appointment_date == today_date.strftime("%d/%m/%Y"):
        #     print(f"today")
        # else:
        #     print(f"not today")

        print(f"appointment_date: {appointment_date}, default_start_date : {default_start_date}")
        print(f"appointment_day: {appointment_day}")
        # วนลูปเพื่อคำนวณช่วงเวลา
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")
            
            if appointment_day in doc.day:
                if start_time_str in appoint_time :
                    updated_times.append((start_time_str, end_time_str, "appointment"))
                elif (appointment_date == datetime.strptime(default_start_date, '%d/%m/%Y')):
                    # ตรวจสอบว่าเวลาปัจจุบันน้อยกว่าเวลาที่กำหนดไว้ (now)
                    if current_time < today:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                    elif start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                        updated_times.append((start_time_str, end_time_str, "in_range"))
                    else:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                else:
                    updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time

        # แปลง doc.day เป็น JSON เพื่อใช้ใน JavaScript
        doc_days_json = mark_safe(json.dumps(doc.day))
        # print(f"updated_times: {updated_times}")

        # ส่งข้อมูลไปยัง template
        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            # 'form': form,  # ฟอร์มนัดหมาย
            'previous': previous,  # หน้าที่มาก่อน
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'default_start_date': default_start_date,  # ส่งวันที่ที่หมอว่างวันแรกไปยัง template,
            'today_day' : today_day,
            'today_date': today_date.strftime("%d/%m/%Y"),
            'appointment_date_str': appointment_date_str,
        }

        return render(request, 'doc_appointment.html', context)

    def post(self, request, current_date):
        appointment_time = request.POST.get('appointment_time')
        # ทำงานกับเวลานัดหมายที่ได้รับมา
        print(f"เวลานัดหมายที่เลือกคือ: {appointment_time}")
        # ส่งค่าหรือบันทึกข้อมูลในฐานข้อมูลได้ตามต้องการ
        return redirect('appoint:doc_appointment_edit', current_date=current_date, appointment_time=appointment_time)

class DoctorAppointmentEditView(LoginRequiredMixin,View):
    def get(self, request, current_date, appointment_time):
        app = Appointment.objects.get(appointment_date=current_date, doctor=request.user, appointment_time=appointment_time)
        print("hi")
        print(f"ผู้ป่วย: {app.patient}")
        app_patient = Patient.objects.get(user=app.patient)
        form = AppointmentForm(instance=app)
        doc = Doctor.objects.get(user=request.user)
        week = range(1, 8)
        today = datetime.now()
        # today = datetime(2024, 10, 16, 9, 30)
        appointment_date = datetime.strptime(current_date, '%Y-%m-%d')
        appointment_date_str = appointment_date.strftime("%d/%m/%Y")

        # Query ที่กรองตาม doctor และวันที่นัดหมาย
        appointments = Appointment.objects.filter(doctor=request.user, appointment_date=appointment_date)

        # ดึงฟิลด์ appointment_time และแปลงเวลาให้อยู่ในรูป %H:%M
        appoint_time = [
            appointment_time.strftime('%H:%M') for appointment_time in appointments.values_list('appointment_time', flat=True)
        ]

        # หาว่าวันนี้คือวันอะไร เอาไปเทียบกับ doc.day เพื่อดูว่าหมอคนที่อยู่ในเวรมั้ย
        appointment_day = appointment_date.strftime("%a")
        today_day = today.strftime("%A")
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



        # หาเป็นวันที่หมอคนนี้จะเริ่มทำงาน
        day_translation = {
            "Mon": "จ.",
            "Tue": "อ.",
            "Wed": "พ.",
            "Thu": "พฤ.",
            "Fri": "ศ.",
            "Sat": "ส.",
            "Sun": "อา."
        }

        appointment_day = day_translation.get(appointment_day)

        #หาช่วงวันที่หมอทำงาน 
        weekdays_full = ["จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์"]
        weekdays_short = ["จ.", "อ.", "พ.", "พฤ.", "ศ.", "ส.", "อา."]
        start_day, end_day = doc.shift_day.split('-') #แยกวันที่เริ่มเวร, วันสุดท้ายของเวรใน 1 สัปดาห์
        start_index = weekdays_full.index(start_day)
        end_index = weekdays_full.index(end_day)
        # สร้างลิสต์เก็บวันเป็นตัวย่อ
        if start_index <= end_index:
            doc.day = weekdays_short[start_index:end_index + 1]
        else:
            doc.day = weekdays_short[start_index:] + weekdays_short[:end_index + 1]
        print(f"doc.day= {doc.day}")




        today_date = today.date()
        days_ahead = 0
        max_days_to_check = 7  # ภายใน 1 สัปดาห์
        default_start_date = None  # ค่าเริ่มต้น

        while days_ahead < max_days_to_check:
            day_eng = today_date.strftime("%a")  
            day_short = day_translation.get(day_eng)
            
            print(f"กำลังตรวจสอบวันที่: {today_date}, day_short: {day_short}")

            if day_short in doc.day:
                default_start_date = today_date.strftime("%d/%m/%Y")  # แปลงวันที่ให้เป็นรูปแบบ dd/mm/yyyy
                break
            today_date += timedelta(days=1)  # ถ้าหมอไม่ว่างในวันนี้ ให้เช็ควันถัดไป
            days_ahead += 1  # เพิ่มตัวนับจำนวนวันที่ตรวจสอบ

        if not default_start_date:
            # กรณีที่ไม่เจอวันว่างเลยใน 7 วันถัดไป
            default_start_date = today.strftime('%d/%m/%Y')  # ใช้วันที่ปัจจุบันแทน

        # เช็คหน้าก่อนว่ามาจากหน้าไหน
        referrer = request.META.get('HTTP_REFERER')
        previous = ""
        if referrer:
            if "appointment" in referrer:
                previous = "คิวพบแพทย์"
            elif "doctor-list" in referrer:
                previous = "รายชื่อแพทย์"
        





        # กำหนดค่าเริ่มต้นและช่วงเวลา
        interval = 10  # นาที
        updated_times = []

        # ใช้วันที่ปัจจุบันและเวลา 08:00
        current_time = datetime.combine(appointment_date, datetime.strptime("08:00", "%H:%M").time())

        # ใช้วันที่ปัจจุบันและเวลา 18:00
        end_time = datetime.combine(appointment_date, datetime.strptime("18:00", "%H:%M").time())

        # เวลาปัจจุบัน (รวมวันที่และเวลา)
        # appointment_date = request.POST.get('appointment_date')
        # if appointment_date is None:
        #     appointment_date = default_start_date

        # print(f"appointment_date:{appointment_date}, today_date: {today_date.strftime("%d/%m/%Y")}")

        # ช่วงเวลาเข้าเวร
        start_bound = datetime.combine(appointment_date, doc.start_time)
        end_bound = datetime.combine(appointment_date, doc.end_time)


        # if appointment_date == today_date.strftime("%d/%m/%Y"):
        #     print(f"today")
        # else:
        #     print(f"not today")

        print(f"appointment_date: {appointment_date}, default_start_date : {default_start_date}")
        print(f"appointment_day: {appointment_day}")
        # วนลูปเพื่อคำนวณช่วงเวลา
        while current_time < end_time:
            start_time_str = current_time.strftime("%H:%M")
            next_time = current_time + timedelta(minutes=interval)
            end_time_str = next_time.strftime("%H:%M")
            
            if appointment_day in doc.day:
                if start_time_str in appoint_time :
                    updated_times.append((start_time_str, end_time_str, "appointment"))
                elif (appointment_date == datetime.strptime(default_start_date, '%d/%m/%Y')):
                    # ตรวจสอบว่าเวลาปัจจุบันน้อยกว่าเวลาที่กำหนดไว้ (now)
                    if current_time < today:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                    elif start_bound <= current_time < end_bound and start_bound < next_time <= end_bound:
                        updated_times.append((start_time_str, end_time_str, "in_range"))
                    else:
                        updated_times.append((start_time_str, end_time_str, "out_of_range"))
                else:
                    updated_times.append((start_time_str, end_time_str, "in_range"))
            else:
                updated_times.append((start_time_str, end_time_str, "out_of_range"))

            # อัปเดต current_time เพื่อทำงานต่อในรอบถัดไป
            current_time = next_time

        # แปลง doc.day เป็น JSON เพื่อใช้ใน JavaScript
        doc_days_json = mark_safe(json.dumps(doc.day))
        # print(f"updated_times: {updated_times}")

        # ส่งข้อมูลไปยัง template
        context = {
            'doc': doc,  # ข้อมูลหมอ
            'week': week,  # ข้อมูลสัปดาห์
            'start': doc.start_time.strftime("%H:%M"),  # เวลาเริ่มทำงานของหมอ
            'end': doc.end_time.strftime("%H:%M"),  # เวลาสิ้นสุดการทำงานของหมอ
            # 'form': form,  # ฟอร์มนัดหมาย
            'previous': previous,  # หน้าที่มาก่อน
            'updated_times': updated_times,  # ช่วงเวลาที่สามารถนัดได้
            'doc_days_json': doc_days_json,  # ส่งข้อมูล doc.day ในรูปแบบ JSON ไปยัง JavaScript
            'default_start_date': default_start_date,  # ส่งวันที่ที่หมอว่างวันแรกไปยัง template,
            'today_day' : today_day,
            'today_date': today_date.strftime("%d/%m/%Y"),
            'appointment_date_str': appointment_date_str,
            'app': app,
            'app_patient':app_patient,
            'current_date':current_date
        }

        return render(request, 'doc_appointment_edit.html', context)