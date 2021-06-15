from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("<h3 align='center'>HOME PAGE APP_1</h3>")

def about(request):
    return HttpResponse("<h3 align='center'>ABOUT PAGE APP_1</h3>")
