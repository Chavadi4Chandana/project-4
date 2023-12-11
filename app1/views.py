from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def god(request):
    return HttpResponse('<h1><marquee>hi how are you</h1></marquee>')
