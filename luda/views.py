from django.shortcuts import render
import os


# Create your views here.

def test(request):
    ret_list = os.listdir("./static/images/")
    return render(request, 'luda/main.html', {'my': ret_list})
