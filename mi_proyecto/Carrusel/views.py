from django.shortcuts import render
def carrusel(request):
    return render(request, 'carrusel/home.html')