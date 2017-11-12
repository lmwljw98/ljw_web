from django.shortcuts import render
from .models import *
from .forms import Captureform
from selenium import webdriver

# Create your views here.

def capture(request):
	
    if 'OK' in request.POST:

        Capture.objects.all().delete()
        Export.objects.all().delete()

        form = Captureform(request.POST)

        my_img = form.save()

        driver = webdriver.PhantomJS(service_args=['--proxy=88.157.149.250:8080', '--proxy-type=http', '--ignore-ssl-errors=true'])
        driver.maximize_window()

        driver.get(str(my_img.imglink))
        driver.save_screenshot('./static/sshot.png')

        driver.close()
        c = Export(src="http://이.정우.메인.한국/static/sshot.png")
        c.save()

        return render(request, 'capture/capture.html', {'link': Capture.objects.all(), 'export': Export.objects.all(), 'form' : form})

    else:

        form = Captureform()
        return render(request, 'capture/capture.html', {'form': form})
