from django.shortcuts import render
import os
import random
from luda.models import My, Gmy


# Create your views here.

def test(request):
    entry_list = list(My.objects.values_list('image_name', flat=True))
    entry_list2 = list(Gmy.objects.values_list('gif_name', flat=True))
    # for i in range(len(entry_list)):
    #    entry_list[i] = entry_list[i].replace("&#39;", "'")
    random.shuffle(entry_list)
    random.shuffle(entry_list2)
    return render(request, 'luda/main.html', {'my': entry_list, 'my2': entry_list2})


def db(request):
    My.objects.all().delete()
    ret_list = os.listdir("./static/images/")
    ret_list2 = os.listdir("./static/gif/")
    for i in range(len(ret_list)):
        q = My(image_name=ret_list[i])
        q.save()
    for i in range(len(ret_list2)):
        q = Gmy(gif_name=ret_list2[i])
        q.save()
    return render(request, 'luda/main.html')
