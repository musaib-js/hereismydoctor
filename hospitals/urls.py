from django.urls import path, include

from . import views


urlpatterns = [
    path('patientsignup/', views.PatientSignup, name = "Patient Signup"),
    path('login/', views.handleLogin, name = "Login"),
    path('logout/', views.handleLogout, name = "Logout"),
    path('create-patient-profile/', views.createProfile, name = "Patient Profile"),
    path('hospitals/', views.hospitals, name = "hospitals"),
    path('hospitals/<int:pk>/', views.hospitaldetails, name = "hospitaldetails"),
    path('doctors/<int:pk>/', views.doctordetails, name = "doctordetail"),
    path('hospital-home/', views.hospitaldashboard, name = "hospitaldashboard"),
    path('add-doctor/', views.addDoctor, name = "addDoctor"),
    path('search-doctor/', views.doctorSearch, name = "search-doctor"),
    path('search-hospital/', views.hospitalSearch, name = "search-hospital"),
    path('appointment-booking/', views.appointmentBooking, name = "appointment"),
    path('our-appointments/', views.appointments, name = "appointments"),
]
