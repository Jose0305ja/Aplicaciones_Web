from django.shortcuts import render

# Create your views here.

def segundo(request):
    return render(request, 'aplicacion1/segundo.html')