from django.urls import path, include

from . import views


urlpatterns = [
    path('patientsignup/', views.PatientSignup, name = "Patient Signup"),
    path('login/', views.handleLogin, name = "Login"),
    path('create-patient-profile/', views.createProfile, name = "Patient Profile"),
    path('hospitals/', views.hospitals, name = "hospitals"),
    path('hospitals/<int:pk>/', views.hospitaldetails, name = "hospitaldetails"),
    path('hospital-home/', views.hospitaldashboard, name = "hospitaldashboard"),
    path('add-doctor/', views.addDoctor, name = "addDoctor"),
    path('search-doctor/', views.doctorSearch, name = "search-doctor"),
    path('search-hospital/', views.hospitalSearch, name = "search-hospital"),
]
