from django.shortcuts import render
import os


# Create your views here.

def test(request):
    return render(request, 'luda/main.html', {'list': os.listdir("./static/images/")})
