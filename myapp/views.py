from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin.html')

def pace2022(request):
    return render(request, 'pace2022.html')

def pace2023(request):
    return render(request, 'pace2023.html')

def pace2024(request):
    return render(request, 'pace2024.html')