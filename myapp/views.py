from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def admin(request):
    return render(request, 'admin.html')

def pace2023(request):
    return render(request, 'PACE2023.html')