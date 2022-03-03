from .models import student
from django import forms
from django.forms import ModelForm
class Student_Registration(ModelForm):
    class Meta:
        model=student
        fields='__all__'