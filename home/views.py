from django.shortcuts import render
from django.http import HttpResponse
from hospitals.models import Hospital

# Create your views here.
def home(request):
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals}
    return render(request, 'index.html', context)