from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
  # return HttpResponse('Welcome to the Health App')
  return render(request, 'index.html')

def about_us(request):
  return render(request, 'about.html')

def blog(request):
  return render(request, 'blog.html')

def dashboard(request):
  return render(request, 'dashboard.html')

def individual(request):
  return render(request, 'individual.html')

def register(request):
  return render(request, 'register.html')

def login(request):
  return render(request, 'login.html')