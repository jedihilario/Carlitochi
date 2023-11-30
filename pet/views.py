from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Pet

# Create your views here.

foods = {
    'default': {
        'hambre': 0,
        'salud': 0
    },
    'creatine': {
        'hambre': -3,
        'salud': 0
    },
    'chicken': {
        'hambre': -15,
        'salud': 0
    },
    'pasta' : {
        'hambre': -10,
        'salud': 0
    },
    'salad': {
        'hambre': -3,
        'salud': 0
    },
    'burger': {
        'hambre': -15,
        'salud': -3
    },
    'fernet': {
        'hambre': -2,
        'salud': -5
    },
    'viagra': {
        'salud': -13,
        'hambre': 0
    },
    'laxante': {
        'salud': -16,
        'hambre': 13
    }
}

def signup (request):
    if (request.method == 'POST'):
        try:
            user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'])
            user.save()
            return redirect('/admin')
        except:
            return render(request, 'pages/signup.html', { 'failed': True })

    return render(request, 'pages/signup.html', { 'failed': False })

def login_req (request):
    if (request.method == 'POST'):
        try:
            user = authenticate(username = request.POST['username'], password = request.POST['password'])
            if (user != None):
                login(request, user)
                return redirect('/home')
            else:
                raise Exception('Login failed')
        except:
            return render(request, 'pages/login.html', { 'failed': True })

    return render(request, 'pages/login.html', { 'failed': False })

def logout_req (request):
    logout(request)
    return redirect('/login')

def home (request):
    if (request.user.is_authenticated):
        name = Pet.objects.get(nombre = 'elpepe')
        return render(request, 'pages/home.html', { 'nombre': name })
    else:
        return redirect('/error')

def eat (request):
    if (request.user.is_authenticated):
        pet = Pet.objects.get(nombre = 'elpepe')

        if (request.method == 'POST'):
            f = 'default'

            for i in request.POST.keys():
                if (i in foods): f = i; break

            pet.hambre += foods[f]['hambre']
            pet.salud += foods[f]['salud']
            pet.save()
            return redirect('/stats')

        return render(request, 'pages/eat.html', { 'nombre': pet.nombre })
    else:
        return redirect('/error')

def bathroom (request):
    if (request.user.is_authenticated):
        name = Pet.objects.get(nombre = 'elpepe')
        return render(request, 'pages/bathroom.html', { 'nombre': name })
    else:
        return redirect('/error')

def stats (request):
    if (request.user.is_authenticated):
        pet = Pet.objects.get(nombre = 'elpepe')
        return render(request, 'pages/stats.html', {
            'nombre': pet.nombre,
            'hambre': pet.hambre,
            'salud': pet.salud,
            'diversion': pet.diversion
    })
    else:
        return redirect('/error')

def error (request):
    return render(request, 'pages/error.html', status=404)