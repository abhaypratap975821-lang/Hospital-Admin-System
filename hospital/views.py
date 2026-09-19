
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from.models import *



def About(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def Index(request):
    return render(request, 'index.html')


def Admin_Dashboard(request):

    if not request.user.is_staff:
        return redirect('login')

    total_doctors = Doctor.objects.count()
    total_patients = Patient.objects.count()
    total_appointments = Appointment.objects.count()

    recent_appointments = Appointment.objects.select_related(
        'doctor',
        'patient'
    ).order_by('-id')[:5]

    return render(request, 'admin_dashboard.html', {
        'total_doctors': total_doctors,
        'total_patients': total_patients,
        'total_appointments': total_appointments,
        'recent_appointments': recent_appointments,
    })


def Login(request):

    error = ""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)




def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)

def Add_Doctor(request):

    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        n = request.POST.get('name')
        c = request.POST.get('contact')
        sp = request.POST.get('special')

        try:
            Doctor.objects.create(
                name=n,
                phone=c,
                speciality=sp
            )

            return redirect('view_doctor')

        except Exception as e:
            print("ERROR:", e)
            return render(request, 'add_doctor.html', {'error': 'yes'})

    return render(request, 'add_doctor.html')


def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')


def Add_patient(request):

    error = ""

    if request.method == "POST":

        name = request.POST.get("name")
        gender = request.POST.get("gender")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")

        try:
            Patient.objects.create(
                name=name,
                gender=gender,
                mobile=mobile,
                address=address
            )
            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    d = {'error': error}
    return render(request, 'add_patient.html', d)





def View_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)


def Delete_Patient(request, pid):
    try:
        patient = Patient.objects.get(id=pid)
        patient.delete()
    except Patient.DoesNotExist:
        pass

    return redirect('view_patient')




def Add_Appointment(request):

    error = ""

    doctor = Doctor.objects.all()
    patient = Patient.objects.all()

    if request.method == "POST":

        doctor_id = request.POST.get("doctor")
        patient_id = request.POST.get("patient")
        date1 = request.POST.get("date1")
        time1 = request.POST.get("time1")

        try:
            doctor_obj = Doctor.objects.get(id=doctor_id)
            patient_obj = Patient.objects.get(id=patient_id)

            Appointment.objects.create(
                doctor=doctor_obj,
                patient=patient_obj,
                date1=date1,
                time1=time1
            )

            error = "no"

        except Exception as e:
            print(e)
            error = "yes"

    d = {
        'doctor': doctor,
        'patient': patient,
        'error': error
    }

    return render(request, 'add_appointment.html', d)


def View_Appointment(request):

    appointment = Appointment.objects.all()

    d = {
        'appointment': appointment
    }

    return render(request, 'view_appointment.html', d)

def Delete_Appointment(request, pid):
    try:
        appointment = Appointment.objects.get(id=pid)
        appointment.delete()
    except Appointment.DoesNotExist:
        pass

    return redirect('view_appointment')




