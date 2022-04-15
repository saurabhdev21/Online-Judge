from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('contact/', views.contact, name = 'contact'),
    path('', views.dashboard, name = 'dashboard'),
    path('problems/', views.problems, name = 'problems'),
    path('submit/', views.submit, name = 'submit'),
    path('verdict/', views.verdict, name = 'verdict'),
    path('login/', views.login, name = 'login')
]