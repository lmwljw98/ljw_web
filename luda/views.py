from django.shortcuts import render
import os
import json

# Create your views here.

def test(request):
    ret_list = os.listdir("./static/images/")
    json_list = json.dumps(ret_list)
    return render(request, 'luda/main.html', {'images': json_list})
