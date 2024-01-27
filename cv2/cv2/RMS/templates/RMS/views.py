from django.shortcuts import render,redirect
from django.urls import path
from django.http import HttpResponse


def home(request):
     return render(request,"RMS/home.html")



def login(request):
     return render(request,"RMS/login.html")

def logout(request):
     return render(request,"RMS/logout.html")


def userprofile(request):
     return render(request,"RMS/userprofile.html")

def usercv(request):
     return render(request,"RMS/usercv.html")
def changepassword(request):
     return render(request,"RMS/changepassword.html")
def Editcvinfo(request):
     return render(request,"RMS/Editcvinfo.html")
def usereducation(request):
     return render(request,"RMS/usereducation.html")
def addusereducation(request):
     return render(request,"RMS/addusereducation.html")
def userexperience(request):
     return render(request,"RMS/userexperience.html")
def adduserexperience(request):
     return render(request,"RMS/adduserexperience.html")
def usercertificates(request):
     return render(request,"RMS/usercertificates.html")

def addusercertificates(request):
     return render(request,"RMS/addusercertificates.html")
def userprojects(request):
     return render(request,"RMS/userprojects.html")
def addproject(request):
     return render(request,"RMS/addproject.html")
def edituserbio(request):
     return render(request,"RMS/edituserbio.html")
def uservolant(request):
     return render(request,"RMS/uservolant.html")
def editusercontact(request):
     return render(request,"RMS/editusercontact.html")
def userskills(request):
     return render(request,"RMS/userskills.html")
def addskills(request):
     return render(request,"RMS/addskills.html")




def Edituserprofile(request):
     return render(request,"RMS/Edituserprofile.html")

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
