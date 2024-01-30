from http.client import HTTPResponse
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path

from . import views



urlpatterns = [
    
               path('',views.home, name="home" ),
               
               path('login',views.userLogin, name="login" ),
               
               path('logout',views.userLogout, name="logout" ),

               path('register',views.register, name="register" ),

               path('userprofile',views.userprofile, name="userprofile" ),
               
               path('companyprofile',views.companyprofile, name="companyprofile" ),
               
               path('department',views.department, name="department" ),

             
               path('noti',views.noti, name="noti" ),

                 
              path('companies',views.companies, name="companies" ),

              path('Editprof',views.Editprof, name="Editprof" ),



               path('usercv',views.usercv, name="usercv" ),

               path('changepassword',views.changepassword, name="changepassword" ),

               path('Editcvinfo',views.Editcvinfo, name="Editcvinfo" ),

               path('usereducation',views.usereducation, name="usereducation" ),

                path('addusereducation',views.addusereducation, name="addusereducation" ),

                path('userexperience',views.userexperience, name="userexperience" ),

                path('adduserexperience',views.adduserexperience, name="adduserexperience" ),

                path('usercertificates',views.usercertificates, name="usercertificates" ),

                path('addusercertificates',views.addusercertificates, name="addusercertificates" ),

                path('userprojects',views.userprojects, name="userprojects" ),

                path('addproject',views.addproject, name="addproject" ),

                path('edituserbio',views.edituserbio, name="edituserbio" ),

                path('uservolant',views.uservolant, name="uservolant" ),

                path('editusercontact',views.editusercontact, name="editusercontact" ),

                path('userskills',views.userskills, name="userskills" ),

               path('addskills',views.addskills, name="addskills" ),
                
               path('JobRequirements/',views.JobRequirements, name="JobRequirements" ),

               path('NewJob/',views.NewJob, name="NewJob" ),

               path('Status/',views.Status, name="Status" ),

               path('JobsHistory/',views.JobsHistory, name="JobsHistory" ),

               path('EditRequirements/',views.EditRequirements, name="EditRequirements" ),

               path('UserStatus/',views.UserStatus, name="UserStatus" ),

               path('FinalCvUpdate/',views.FinalCvUpdate, name="FinalCvUpdate" ),

               path('comProfileOut/',views.comProfileOut, name="comProfileOut" ),

               path('userProfileOut/',views.userProfileOut, name="userProfileOut" ),

               path('AddSection1/',views.AddSection1, name="AddSection1" ),

               path('UserOther/',views.UserOther, name="UserOther" ),



] 