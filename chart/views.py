from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
from .models import *

# Create your views here.

def ma_in(request):

    return render(request, 'chart/chart.html')

def chart(request):

    Rank.objects.all().delete()

    naver_list = ["null_index"]
    naver_udlist = ["null_index"]

    naver_html = urllib.request.urlopen("http://www.naver.com")

    naver_soup = BeautifulSoup(naver_html, 'lxml')

    number = 1

    for naver_chart in naver_soup.find_all("span", {"class": "ell"}):

        naver_list.append(naver_chart.string)

    for naver_updown in naver_soup.find_all("span", {"class": "tx"}):

        naver_udlist.append(naver_updown.string)

    while number < 21:

        naver_udlist[number] = naver_udlist[number].replace("상승", "▲")
        naver_udlist[number] = naver_udlist[number].replace("하락", "▼")

        r = Rank(naver_rank=str(number) + "위 : " + naver_list[number] + " [ " + naver_udlist[number] + " ] ")
        r.save()

        number = number + 1

    return render(request, 'chart/naver.html', {'rank': Rank.objects.all()})

def daum(request):

    Rank.objects.all().delete()

    daum_list = []
    daum_udlist = []

    daum_html = urllib.request.urlopen("http://www.daum.net")

    daum_soup = BeautifulSoup(daum_html, 'lxml')

    number_d = 0

    for daum_chart in daum_soup.find_all("span", {"class": "txt_issue"}):

        for daum_chart2 in daum_chart.find_all("a"):

            daum_list.append(daum_chart2.string)

    for da in daum_soup.find_all("span", {"class": "txt_issue"}):

        for da2 in da.find_all("strong"):

            daum_list.append(da2.string)

    daum_list = list(set(daum_list))    # 리스트에 존재하는 중복원소 제거

    for daum_updown in daum_soup.find_all("em", {"class": "num_issue"}):

        for daum_updown2 in daum_updown.find_all("span", {"class": "ir_wa"}):

            daum_udlist.append(daum_updown2.string)

    while number_d < 11:

        daum_udlist[number_d] = daum_udlist[number_d].replace("↑ 상승", "▲")
        daum_udlist[number_d] = daum_udlist[number_d].replace("↓ 하락", "▼")
        daum_udlist[number_d] = daum_udlist[number_d].replace("신규진입", "NEW")

        r = Rank(daum_rank=str(daum_list[number_d]) + " [ " + str(daum_udlist[number_d]) + " ] ")
        r.save()
        Rank.objects.filter(daum_rank__startswith="None").delete()

        number_d = number_d + 1

    return render(request, 'chart/daum.html', {'rank': Rank.objects.all()})

def melon(request):

    Rank.objects.all().delete()

    melon_song = ["null_index"]
    melon_singer = ["null_index"]
    melon_updown_num = ["null_index"]

    melon_html_1 = urllib.request.urlopen("https://www.melon.com/chart/index.htm#params%5Bidx%5D=1")
    melon_soup_1 = BeautifulSoup(melon_html_1, 'lxml')

    melon_html_2 = urllib.request.urlopen("https://www.melon.com/chart/index.htm#params%5Bidx%5D=51")
    melon_soup_2 = BeautifulSoup(melon_html_2, 'lxml')

    melon_time = melon_soup_1.find("span", {"class": "hour type1"})

    for melon_ in melon_soup_1.find_all("div", {"class": "ellipsis rank01"}):
        melon_song.append(melon_.strong.string)

    for melon_ in melon_soup_1.find_all("div", {"class": "ellipsis rank02"}):
        melon_singer.append(melon_.span.string)

    for melon_ in melon_soup_2.find_all("div", {"class": "ellipsis rank01"}):
        melon_song.append(melon_.strong.string)

    for melon_ in melon_soup_2.find_all("div", {"class": "ellipsis rank02"}):
        melon_singer.append(melon_.span.string)

    for melon_ in melon_soup_1.find_all("span", {"class": "wrap_rank"}):

        if melon_.span.string == "단계 상승":

            for melon_up in melon_.find_all("span", {"class": "up"}):
                melon_updown_num.append(" ▲" + melon_up.string + " ")

        elif melon_.span.string == "단계 하락":

            for melon_up in melon_.find_all("span", {"class": "down"}):
                melon_updown_num.append(" ▼" + melon_up.string + " ")

        elif melon_.span.string == "순위 동일":

            melon_updown_num.append(" - ")

        elif melon_.span.string == "NEW":

            melon_updown_num.append(" NEW ! ")

    for melon_ in melon_soup_2.find_all("span", {"class": "wrap_rank"}):

        if melon_.span.string == "단계 상승":

            for melon_up in melon_.find_all("span", {"class": "up"}):
                melon_updown_num.append(" ▲" + melon_up.string + " ")

        elif melon_.span.string == "단계 하락":

            for melon_up in melon_.find_all("span", {"class": "down"}):
                melon_updown_num.append(" ▼" + melon_up.string + " ")

        elif melon_.span.string == "순위 동일":

            melon_updown_num.append(" - ")

        elif melon_.span.string == "NEW":

            melon_updown_num.append(" NEW ! ")

    number = 1

    while number < 101:

        r = Rank(melon_rank=str(number) + "위 : " + melon_song[number] + " - " + melon_singer[number] + " (" + melon_updown_num[number] + ")")
        r.save()

        number = number + 1

    return render(request, 'chart/melon.html', {'rank': Rank.objects.all(), 'time': melon_time.string})