from django.shortcuts import render_to_response
import os
import json


# Create your views here.

def test(request):
    ret_list = os.listdir("./static/images/")
    return render_to_response(request, 'luda/main.html', {"images": json.dumps(ret_list)})
