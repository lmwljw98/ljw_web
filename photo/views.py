from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
from .models import *
from .forms import Linkform

# Create your views here.

rlist = []
plist = []
gallery = "http://gall.dcinside.com"
original = "dcimg1"
original2 = "dcimg2"
original3 = "dcimg3"
changed = "image"

def photo(request):

    global rlist

    if "OK" in request.POST:

        rlist = []

        Mydata.objects.all().delete()

        Links.objects.all().delete()    # 데이터베이스 초기화

        form = Linkform(request.POST)

        my_code = form.save()

        recom_html = urllib.request.urlopen(
            gallery + "/board/lists/?id=" + my_code.code + "&page=" + my_code.page + "&exception_mode=recommend")

        recom_soup = BeautifulSoup(recom_html, 'lxml')

        for recom_link in recom_soup.find_all("a", {"class": "icon_pic_b"}):

            rlist.append(gallery + recom_link.get('href'))

        for i in range(0, 10, 1):

            html = urllib.request.urlopen(rlist[i])

            soup = BeautifulSoup(html, 'lxml')

            for image_link in soup.find_all("div", {"class": "s_write"}):   # div 태그의 s_write라는 이름의 클래스 검색

                for image_link2 in image_link.find_all("img"):

                    plist.append(image_link2.get('src'))

                    plist[0] = plist[0].replace(original, changed)
                    plist[0] = plist[0].replace(original2, changed)
                    plist[0] = plist[0].replace(original3, changed)
                    plist[0] = plist[0].replace("co.kr", "com")

                    q = Links(img = plist[0])
                    q.save()

                    del plist[0:25]

        return render(request, 'photo/photo.html', {'list': Links.objects.all(), 'form': form})  # html 출력

    elif "NEXT" in request.POST:

        for u in range(10, len(rlist), 1):

            html = urllib.request.urlopen(rlist[u])

            soup = BeautifulSoup(html, 'lxml')

            for image_link in soup.find_all("div", {"class": "s_write"}):   # div 태그의 s_write라는 이름의 클래스 검색

                for image_link2 in image_link.find_all("img"):

                    plist.append(image_link2.get('src'))

                    plist[0] = plist[0].replace(original, changed)
                    plist[0] = plist[0].replace(original2, changed)
                    plist[0] = plist[0].replace(original3, changed)
                    plist[0] = plist[0].replace("co.kr", "com")

                    q = Links(img = plist[0])
                    q.save()

                    del plist[0:25]

        return render(request, 'photo/photo2.html', {'list': Links.objects.all()})  # html 출력

    else:

        form = Linkform()
        return render(request, 'photo/photo_f.html', {'form': form})  # html 출력


