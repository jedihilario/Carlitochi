from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

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

def home(request):
    return render(request, 'pages/home.html')