from django.shortcuts import render

def stylist_home(request):
    return render(request, "stylist_templates/home.html")
