from django.shortcuts import render
from .models import Login


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