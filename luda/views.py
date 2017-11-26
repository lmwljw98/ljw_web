from django.shortcuts import render
import os
import json
from luda.models import My


# Create your views here.

def test(request):
    return render(request, 'luda/main.html', {'my': json.dumps(My.objects.all().image_name)})


def db(request):
    ret_list = os.listdir("./static/images/")
    for i in range(len(ret_list)):
        # My.objects.create(image_name=ret_list[i])
        q = My(image_name=ret_list[i])
        q.save()
    return render(request, 'luda/main.html')
