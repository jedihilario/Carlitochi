from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Pet

# Create your views here.

def signup (request):
    if (request.method == 'POST'):
        try:
            user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])
            user.save()
            return redirect('/admin')
        except:
            return render(request, 'pages/signup.html', { 'failed': True })

    return render(request, 'pages/signup.html', { 'failed': False })

def home (request):
    name = Pet.objects.get(nombre = 'elpepe')
    return render(request, 'pages/home.html', { 'nombre': name })

def eat (request):
    name = Pet.objects.get(nombre = 'elpepe')
    return render(request, 'pages/eat.html', { 'nombre': name })

def stats (request):
    pet = Pet.objects.get(nombre = 'elpepe')
    return render(request, 'pages/stats.html', {
        'nombre': pet.nombre,
        'hambre': pet.hambre,
        'salud': pet.salud,
        'diversion': pet.diversion
    })