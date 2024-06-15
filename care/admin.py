from django.contrib import admin
from .models import*

admin.site.register([parent_reg, babysitter, doctor, services, baby_enroll, nutritionists, feedbacks, sitter_request, doctor_request, nutrition_request, attendance, payments, vacinations, baby_info])
# Register your models here.
