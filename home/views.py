from django.shortcuts import render
from django.http import HttpResponse
from hospitals.models import Hospital, Doctor

# Create your views here.
def home(request):
    hospitals = Hospital.objects.all()
    doctors = Doctor.objects.all()
    context = {'hospitals': hospitals, 'doctors': doctors}
    return render(request, 'index.html', context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "service.html")

def contact(request):
    return render(request, "contact.html")