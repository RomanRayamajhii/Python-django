from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Hello Roman!")
def about(request):
    return HttpResponse("Hello Pranisha")
def post(request,post_id):
    return HttpResponse(f"post page </br> <h1>{post_id}</h1>")
def user(request,username):
    return HttpResponse(f"user page </br> <h1>{username}</h1>")
