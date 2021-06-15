from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
	return HttpResponse("<h2 align='center'>HOME PAGE APP_1</h2>")

def about(request):
    return HttpResponse("<h2 align='center'>ABOUT PAGE APP_1</h2>")

def product(request):
    return HttpResponse("<h2 align='center'>PRODUCT PAGE APP_1</h2>")

def customer(request):
    return HttpResponse("<h2 align='center'>CUSTOMER PAGE APP_1</h2>")
