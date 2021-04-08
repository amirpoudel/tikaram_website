from django.shortcuts import render
from .models import Report

def home(request):
    
    return  render(request , 'home.html')


def service(request):
    return render(request , 'service.html')


def about(request):
    return render(request, 'about.html')


def report(request):
    reports = Report.objects.all()
    return render(request, 'report.html' ,{'reports':reports})

def contact(request):
    return render(request, 'contact.html')
