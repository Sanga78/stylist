from django.shortcuts import render

def client_home(request):
    return render(request, "client_templates/home.html")
