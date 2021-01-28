from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def welcome(request):
    ##return HttpResponse("Welcome to the Meeting Planner!, this is a test page")
    return render(request, "website/welcome.html", 
    {"message": "This is a test", "link":"http://www.yahoo.com"}
    )

def date(request):
    return HttpResponse("Welcome! This page was served at " + str(datetime.now()))
# Create your views here.


def about(request):
    return HttpResponse("This is the about page.")