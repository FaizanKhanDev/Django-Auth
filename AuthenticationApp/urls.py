from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('SingUp/', views.SingUp, name='SingUp'),
    path('Login/', views.Login, name='Login'),
    path('Logout/', views.Logout, name="Logout"),
    path('userProfileUpdate/', views.UserProfileUpdate, name="userProfileUpdate"),
    path('ForgetPassword/', views.ForgetPassword, name="ForgetPassword"),
    path('ChangePassword/<token>/', views.ChangePassword, name="ChangePassword"),


    path('SearchProduct/', views.SearchProductView, name="SearchProduct")


    
    
]
