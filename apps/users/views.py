
from django.shortcuts import render, HttpResponse, redirect
def register(request):
  response = "placeholder for users to create a new user record"
  return HttpResponse(response)

def log(request):
  response = "placeholder for users to login"
  return HttpResponse(response)

def display(request):
  response = 'placeholder to later display all the list of users'
  return HttpResponse(response)
