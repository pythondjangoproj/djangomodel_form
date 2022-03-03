from django.contrib import admin
from .models import student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','marks','subject']


admin.site.register(student,StudentAdmin)
