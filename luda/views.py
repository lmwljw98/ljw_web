from django.shortcuts import render
import os
import json


# Create your views here.

def test(request):
    ret_list = os.listdir("./static/images/")
    return render(request, 'luda/main.html', images=json.dumps(ret_list))
