from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    ##return HttpResponse("Welcome to the Meeting Planner!, this is a test page")
    return render(request, 'website\template\welcome.html' )