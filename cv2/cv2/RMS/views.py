from django.shortcuts import render,redirect
from django.urls import path
from .models import *
from .forms import CreateNewUser
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required


@login_required(login_url= 'register')
def home(request):
     return render(request,"RMS/home.html")


def userLogin(request):  
     if request.user.is_authenticated:
          return redirect('/')
     else :
          

      if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password.')    


      context = {}
      return render(request, 'RMS/login.html')
   


def userLogout(request):
     logout(request)
     return redirect ('login')



def register (request):
   if request.user.is_authenticated:
          return redirect('/')
   else :
          form = CreateNewUser()
          if request.method == 'POST' :   
                 form = CreateNewUser(request.POST)
                 if form.is_valid():
                         form.save() 
                         user = form.cleaned_data.get('username')
                         messages.success(request ,user+ 'Create Successfully !')
                         return redirect('login')
          context = {'form' : form }
          return render(request ,"RMS/register.html"  ,context )




@login_required(login_url= 'login')
def userprofile(request):
     return render(request,"RMS/userprofile.html")
@login_required(login_url= 'login')
def companyprofile(request):
     return render(request,"RMS/companyprofile.html")

@login_required(login_url= 'login')
def department(request):
     return render(request,"RMS/department.html")


@login_required(login_url= 'login')
def noti(request):
     return render(request,"RMS/noti.html")


@login_required(login_url= 'login')
def companies(request):
     return render(request,"RMS/companies.html")

@login_required(login_url= 'login')
def Editprof(request):
     return render(request,"RMS/Editprof.html")


@login_required(login_url= 'login')
def usercv(request):
     return render(request,"RMS/usercv.html")


@login_required(login_url= 'login')
def changepassword(request):
     return render(request,"RMS/changepassword.html")

@login_required(login_url= 'login')
def Editcvinfo(request):
     return render(request,"RMS/Editcvinfo.html")

@login_required(login_url= 'login')
def usereducation(request):
     return render(request,"RMS/usereducation.html")

@login_required(login_url= 'login')
def addusereducation(request):
     return render(request,"RMS/addusereducation.html")

@login_required(login_url= 'login')
def userexperience(request):
     return render(request,"RMS/userexperience.html")

@login_required(login_url= 'login')
def adduserexperience(request):
     return render(request,"RMS/adduserexperience.html")

@login_required(login_url= 'login')
def usercertificates(request):
     return render(request,"RMS/usercertificates.html")

@login_required(login_url= 'login')
def addusercertificates(request):
     return render(request,"RMS/addusercertificates.html")

@login_required(login_url= 'login')
def userprojects(request):
     return render(request,"RMS/userprojects.html")

@login_required(login_url= 'login')
def addproject(request):
     return render(request,"RMS/addproject.html")

@login_required(login_url= 'login')
def edituserbio(request):
     return render(request,"RMS/edituserbio.html")

@login_required(login_url= 'login')
def uservolant(request):
     return render(request,"RMS/uservolant.html")

@login_required(login_url= 'login')
def editusercontact(request):
     return render(request,"RMS/editusercontact.html")

@login_required(login_url= 'login')
def userskills(request):
     return render(request,"RMS/userskills.html")

@login_required(login_url= 'login')
def addskills(request):
     return render(request,"RMS/addskills.html")

@login_required(login_url= 'login')
def JobRequirements(request):
     return render(request,"RMS/JobRequirements.html")
@login_required(login_url= 'login')
def NewJob(request):
     return render(request,"RMS/NewJob.html")
@login_required(login_url= 'login')
def Status(request):
     return render(request,"RMS/Status.html")
@login_required(login_url= 'login')
def JobsHistory(request):
     return render(request,"RMS/JobsHistory.html")
@login_required(login_url= 'login')
def EditRequirements(request):
     return render(request,"RMS/EditRequirements.html")
@login_required(login_url= 'login')
def UserStatus(request):
     return render(request,"RMS/UserStatus.html")
@login_required(login_url= 'login')
def FinalCvUpdate(request):
     return render(request,"RMS/FinalCvUpdate.html")

@login_required(login_url= 'login')
def comProfileOut(request):
     return render(request,"RMS/comProfileOut.html")

@login_required(login_url= 'login')
def userProfileOut(request):
     return render(request,"RMS/userProfileOut.html")

@login_required(login_url= 'login')
def AddSection1(request):
     return render(request,"RMS/AddSection1.html")

@login_required(login_url= 'login')
def UserOther(request):
     return render(request,"RMS/UserOther.html")
