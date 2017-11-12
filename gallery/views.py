from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def gallery(request):

    if "NEXT" in request.POST:

        form = Gform(request.POST)

        my = form.save()

        if int(my.start) > int(my.end):

            las = Photo.objects.last()
            las.delete()

            return HttpResponse("Error")

        else:

            filters = Photo.objects.all()[int(my.start)-1:int(my.end)]

            las = Photo.objects.last()
            las.delete()

            return render(request, 'gallery/gallery.html', {'my_photo': filters, 'form': form})

    else:

        form = Gform()
        filters = Photo.objects.all()[0:5]

        return render(request, 'gallery/gallery.html', {'my_photo': filters, 'form': form})