from django.contrib import admin
from .models import User, Hospital, Patient, Doctor
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
# Register your models here.
admin.site.register((Hospital, Patient, Doctor))