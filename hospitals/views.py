from django.shortcuts import render, redirect
from .models import User, Hospital, Patient, Doctor, Appointment
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
    doctors  = Doctor.objects.filter(hospital = hospital)
    print(doctors)
    ldeparments = hospital.departments
    departments = ldeparments.split(",")
    context = {'hospital':hospital, 'departments': departments, 'doctors': doctors}
    return render(request, 'hospitaldetail.html', context)

def doctordetails(request, pk):
    doctor = Doctor.objects.filter(pk = pk)[0]
    newlist = list(doctor.hospital.values())
    hospitals=[]
    for i in newlist:
        hospitals.append(i['name'])
    context = {'doctor': doctor,'hospitals':hospitals}
    return render(request, 'doctordetail.html', context)

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

def doctorSearch(request):
    query=request.GET['query']
    if len(query)>300:
        allDoctors=Doctor.objects.none()
    else:
        allDoctorsName= Doctor.objects.filter(name__icontains=query)
        allDoctors=  allDoctorsName
        for a in allDoctors:
            print(a.hospital)
    if allDoctors.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    context={'allDoctors': allDoctors, 'query': query}
    return render(request, 'doctorsearch.html', context)

def hospitalSearch(request):
    query=request.GET['query']
    if len(query)>300:
        allHospitals=Hospital.objects.none()
    else:
        allHospitalsName= Hospital.objects.filter(name__icontains=query)
        allHospitals=  allHospitalsName
    if allHospitals.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    context={'allHospitals': allHospitals, 'query': query}
    return render(request, 'hospitalsearch.html', context)

@login_required    
def appointmentBooking(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            date = request.POST['date']
            doctor = request.POST.get('doctor')
            hospital = request.POST['hospital']
            hospital_instance = Hospital.objects.get(name = hospital)
            doctor_instance = Doctor.objects.get(pk = doctor)
            patient = Patient.objects.filter(user = request.user)[0]
            newAppointment = Appointment(patient = patient, date = date, doctor = doctor_instance, hospital = hospital_instance)
            newAppointment.save()
            messages.success(request, "Appointment Booked Successfully. Kindly wait for confirmation")
            return redirect('/')
        else:
            return redirect('/medicare/login')

def appointments(request):
    hospital = Hospital.objects.get(user = request.user)
    appointments = Appointment.objects.filter(hospital = hospital)
    print(appointments)
    context = {'appointments': appointments}
    return render(request, 'hospitalappointments.html', context)

def handleLogout(request):
    logout(request)
    return redirect('/medicare/login')