from django.shortcuts import render
from django.http import HttpResponse
import random
from .models import Project # Импортируем модель проекта

def home(request):
    projects = Project.objects.all() # Импортируем все записи о проектах из базы данных
    return render(request, 'portfolio/home.html', {'projects':projects} ) # Используя переменную projects, передаем словарь в шаблом с ключем projects и значением: список projects выше
def about(request):
    return render (request, 'portfolio/about.html')

def password_generator(request):
    return render(request, 'portfolio/password_generator.html')

def login(request):
    return render(request, 'portfolio/login.html')

def your_password(request):

    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('lenght', 12))

    thepassword = ''
    for  x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'portfolio/your_password.html', {'password': thepassword})