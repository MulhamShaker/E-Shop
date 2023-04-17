from django.shortcuts import render
from .models import Login
from .models import Signup


def home(request):
    return render (request, "pages/home.html")
    


def login(request):
    if request.method == "POST":
        data = Login(request.POST)
        if data == True:
            data.save()
    username = request.POST.get("username")
    password = request.POST.get("password")
    print(username , password)
    data = Login(username = username , password = password)
    return render(request, "pages/login.html")



def signup(request):
    if request.method == "POST":
        data = Signup(request.POST)
        if data == True:
            data.save()
    firstname = request.POST.get("firtsname")
    lastname = request.POST.get("lastname")
    password = request.POST.get("password")
    email = request.POST.get("email")
    print(firstname,lastname, password, email)
    data = Signup(firstname = firstname, lastname = lastname, password = password, email = email)
    return render(request, "pages/signup.html")