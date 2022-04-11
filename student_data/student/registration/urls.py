from django.urls import path
from . import  views

urlpatterns = [
    path('home/', views.homepage, name='home'),
    path('savedata/dashboard/', views.dashboard, name='dashboard'),
    path('savedata/', views.StudentRegistration, name='savedata'),

]
