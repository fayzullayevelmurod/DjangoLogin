from django.shortcuts import render, redirect
from .models import Register
from django.http.response import HttpResponse
# Create your views here.
def homepage(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        user=Register(username=username, email=email, password=password)
        user.save()
        return redirect('/')
    else:
        return render(request, 'register.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if Register.objects.filter(username=username, password=password).exists():
            return redirect('/')
        else:
            return HttpResponse('Username yoki Password xato')
    else:
        return render(request, 'login.html')