from django.shortcuts import render
import json
import urllib.request
from .models import *
from .forms import *
from ipware.ip import get_ip

# Create your views here.

url = "http://freegeoip.net/json/"

def geoip(request):

    if "OK" in request.POST:

        form = Inputform(request.POST)

        userInput = form.save()

        user_html = urllib.request.urlopen(url + userInput.input)

        data = user_html.read()

        convert_json = json.loads(data.decode('utf-8'))
        
        ip = convert_json["ip"]

        c_c = convert_json["country_code"]
        c_n = convert_json["country_name"]
        r_c = convert_json["region_code"]
        r_n = convert_json["region_name"]
        city = convert_json["city"]
        z_c = convert_json["zip_code"]
        t_z = convert_json["time_zone"]
        la = convert_json["latitude"]
        long = convert_json["longitude"]
        m_c = convert_json["metro_code"]

        return render(request, 'geoip/geoip.html', 
                {'ip': ip, 'c_c': c_c, 'c_n': c_n,
            'r_c': r_c, 'r_n': r_n, 'city': city, 'z_c': z_c, 't_z': t_z, 'la': la, 
            'long': long, 'm_c': m_c})

    else:
        ip = get_ip(request)
        form = Inputform()
        return render(request, 'geoip/geoip_f.html', {'ip': ip, 'form': form})
