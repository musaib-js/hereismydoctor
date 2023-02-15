from django.db import models
from django.contrib.auth.models import AbstractUser

#Abstract User Model
class User(AbstractUser):
    is_patient = models.BooleanField('Patient Status', default=False)
    is_hospital = models.BooleanField('Hospital Status', default=False)

STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattisgarh','Chhattisgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pradesh','Himachal Pradesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Kerala','Kerala'),
  ('Lakshadweep','Lakshadweep'),
  ('Madhya Pradesh','Madhya Pradesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalaya','Meghalaya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Punjab','Punjab'),
  ('Rajasthan','Rajasthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('West Bengal','West Bengal'),
)

HOSPITAL_CHOICES = (
    ('Dispensary', 'Dispensary'),
    ('Sub-District Hospital', 'Sub District Hospital'),
    ('District Hospital', 'District Hospital'),
    ('Superspeciality Hospital', 'Superspeciality Hospital')
)

# Create your models here.
class Hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length = 500)
    state = models.CharField(choices=STATE_CHOICES, max_length=80)
    district = models.CharField(max_length=80)
    location = models.CharField(max_length = 250)
    type = models.CharField(choices=HOSPITAL_CHOICES ,max_length = 150)
    total_doctors = models.IntegerField(default=0)
    total_paramedics = models.IntegerField(default=0)
    total_beds = models.IntegerField(default = 0)
    total_departments = models.IntegerField(default=0)
    departments = models.TextField(default = "General")

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    hospital = models.ManyToManyField(Hospital, related_name="hospital")
    duty_time = models.CharField(max_length=150)
    OPD_time = models.CharField(max_length=150)
    room_number = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 10)
    age = models.IntegerField()
    address = models.CharField(max_length = 200)
    aadhar_number = models.IntegerField()

    def __str__(self):
        return self.full_name
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient)
    