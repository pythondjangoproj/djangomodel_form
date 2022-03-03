from django.shortcuts import render,redirect
from .models import student
from . import forms
from . import serializer
from .serializer import student_serializer
import requests
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

def Student_info(request):
    form=forms.Student_Registration()
    if request.method=='POST':
        form=forms.Student_Registration(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/home/')
    return render(request,'modelform_app/index.html',{'form':form})

def Student_database(request):
    St_data=student.objects.all()
    return render(request,'modelform_app/register.html',{'St_data':St_data})

class Student_serialise(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = student_serializer