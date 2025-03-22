from django.shortcuts import render
from .models import WomenInTech

def home_view(request):
    return render(request, 'home/home.html')

def home(request):
    women = WomenInTech.objects.all()
    return render(request, 'home/home.html', {'women': women})