from django.shortcuts import render
import os
import json


# Create your views here.

def test(request):
    ret_list = os.listdir("./static/images/")
    return render(request, 'luda/main.html', {'my': [1, 2, 3, 4, 5, 6]})
