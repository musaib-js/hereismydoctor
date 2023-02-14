from django.shortcuts import render, redirect
from .models import User, Hospital, Patient, Doctor
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def PatientSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        email = request.POST['email']
        if password == cpassword:
            newuser = User.objects.create_user(username = username, password = password, email = email, is_patient = True)
            newuser.save()
            login(request, newuser)
            messages.success(request, " Your Account! has been created successfully")
            return redirect('/medicare/create-patient-profile')
        else:
            messages.error(request, "Passwords don't match")
            return redirect('/medicare/patientsignup')
    return render(request, 'signup.html')

def createProfile(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['address']
        aadhar_number = request.POST['aadhar_number']

        newProfile = Patient.objects.create(user = request.user, full_name = full_name, gender = gender, age =  age, address = address, aadhar_number = aadhar_number)
        newProfile.save()
        return redirect('/')
    return render(request, 'createProfile.html')

def handleLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username  = username, password = password)  
        if user is not None:
            login(request, user)
            if request.user.is_patient:
                messages.success(request, "Logged in Successfully")
                return redirect('/')
            elif request.user.is_hospital:
                messages.success(request, "Hospital Login Successfull")
                return redirect('/medicare/hospital-home')
            
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/medicare/login')
    return render(request, 'login.html')

def hospitals(request):
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'hospitals.html', context)

def hospitaldetails(request, pk):
    hospital = Hospital.objects.filter(pk = pk)[0]
    doctors  = Doctor.objects.filter(hospital = pk)
    print(doctors)
    ldeparments = hospital.departments
    departments = ldeparments.split(",")
    context = {'hospital':hospital, 'departments': departments, 'doctors': doctors}
    return render(request, 'hospitaldetail.html', context)

@login_required
def hospitaldashboard(request):
    hospital = Hospital.objects.filter(user = request.user).first()
    ldeparments = hospital.departments
    departments = ldeparments.split(",")
    doctors = Doctor.objects.filter(hospital = hospital)
    context = {'hospital': hospital, 'doctors': doctors, 'departments': departments}
    return render(request, 'hospitaldashboard.html', context)

@login_required
def addDoctor(request):
    if request.method == "POST":
        name = request.POST['name']
        qualification = request.POST['qualification']
        department = request.POST['department']
        duty_time = request.POST['duty_time']
        opd_time = request.POST['opd_time']
        room_num = request.POST['room_num']
        hospital = Hospital.objects.filter(user = request.user)

        newdoc = Doctor.objects.create(name = name, qualification = qualification, department = department, duty_time = duty_time, OPD_time = opd_time, room_number = room_num)
        newdoc.hospital.set(hospital)
        newdoc.save()
        messages.success(request, "Doctor Added Successfully")
        return redirect('/medicare/hospital-home')
    