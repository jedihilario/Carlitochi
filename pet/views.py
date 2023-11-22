from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def signup (request):
    if (request.method == 'POST'):
        return redirect('/admin')

    return render(request, 'pages/signup.html')