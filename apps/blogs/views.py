from django.shortcuts import render, HttpResponse, redirect
def index(request):
  response = "placeholder to later display all the list of blogs"
  return HttpResponse(response)

def new(request):
  response = "placeholder to display a new form to create a new blog"
  return HttpResponse(response)

def redi(request):
  return redirect('/blogs')

def show(request, number):
  return HttpResponse("placeholder to display blog {}".format(number))

def edit(request, number):
  response = "placeholder to edit blog {}".format(number)
  return HttpResponse(response)

def destroy(request, number):
  response = "placeholder to delete blog {}".format(number)
  return HttpResponse(response)


