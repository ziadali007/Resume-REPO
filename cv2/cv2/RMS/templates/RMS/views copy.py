from django.shortcuts import render,redirect
from django.urls import path
from django.http import HttpResponse,HttpResponseRedirect


def home(request):
     return render(request,"RMS/home.html")



def login(request):
     return render(request,"RMS/login.html")

def logout(request):
     return render(request,"RMS/logout.html")


def userprofile(request):
     return render(request,"RMS/userprofile.html")

def companyprofile(request):
     return render(request,"RMS/companyprofile.html")

def register(request):
     return render(request,"RMS/register.html")


def department(request):
     return render(request,"RMS/department.html")



def about(request):
     return render(request,"RMS/about.html")


def noti(request):
     return render(request,"RMS/noti.html")

def EditProfile(request):
     return render(request,"RMS/EditProfile.html")

def ComProfile(request):
     return render(request,"RMS/ComProfile.html")

def companies(request):
     return render(request,"RMS/companies.html")

def JobRequirements(request):
     return render(request,"RMS/JobRequirements.html")

def NewJob(request):
     return render(request,"RMS/NewJob.html")

def Status(request):
     return render(request,"RMS/Status.html")

def JobsHistory(request):
     return render(request,"RMS/JobsHistory.html")

