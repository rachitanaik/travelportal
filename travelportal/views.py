from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login

def employee(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        redirect("http://127.0.0.1:8000/employee/")
        
    else:
        returnHttpResponse("Invalid Username and Password")