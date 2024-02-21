from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Anasayfa") 

def siniflar(request):
    return HttpResponse("Kurslarımız")