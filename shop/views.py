from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Welcome to shop")
def product(request):
    return HttpResponse("Product page")
