from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, "home.html")
def text(request):
    return render(request, "index.html")
def form(request):
    return render(request, "form.html")