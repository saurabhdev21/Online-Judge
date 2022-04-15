from django.shortcuts import render

# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')

def contact(request):
    return render(request, 'contact.html')

def problems(request):
    return render(request, 'problems.html')

def submit(request):
    return render(request, 'submit.html')

def login(request):
    return render(request, 'login.html')

def verdict(request):
    return render(request, 'verdict.html')    
