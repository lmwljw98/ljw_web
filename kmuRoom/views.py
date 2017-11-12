from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import json, datetime
import requests


# Create your views here.

def keyboard(request):
    return JsonResponse(

        {
            'type': 'buttons',
            'buttons': ['7호관', '경상관', '경영관', '공학관', '공학관별관', '과학관', '국제관', '법학관', '복지관', '본부관', '북악관', '예술관', '조형관',
                        '조형관별관', '형설관']
        }
    )


def getData(name):
    nowList = []
    hourList = []

    params = {'method': 'getEmptyRoomListAll', 'building': name}
    res = requests.post('http://willbt.com/kmu/ajax/kmuInfoAjax.php', data=params)

    jsonData = res.text \
        .replace("'", '"') \
        .replace("result", '"result"') \
        .replace("name", '"name"')

    roomList = json.loads(jsonData)['result']

    for i in range(len(roomList)):
        nowList.append(roomList[i]['name'])

    params = {'method': 'getEmptyRoomListAll', 'building': name, 'nextTime': 1}
    res = requests.post('http://willbt.com/kmu/ajax/kmuInfoAjax.php', data=params)

    jsonData = res.text \
        .replace("'", '"') \
        .replace("result", '"result"') \
        .replace("name", '"name"')

    roomList = json.loads(jsonData)['result']

    for i in range(len(roomList)):
        hourList.append(roomList[i]['name'])

    now = "\n".join(nowList)
    hour = "\n".join(hourList)

    return "현재 비어있는 강의실\n\n" + now + "\n\n\n1시간 뒤 비어있는 강의실\n\n" + hour


@csrf_exempt
def answer(request):
    today = datetime.datetime.now().strftime("%m월 %d일 %H:%M:%S")
    str = ((request.body).decode('utf-8'))
    received = json.loads(str)
    name = received['content']

    return JsonResponse(
        {
            'message': {
                'text': today + '\n' + name + '의 빈 강의실 목록\n\n' + getData(name)

            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['7호관', '경상관', '경영관', '공학관', '공학관별관', '과학관', '국제관', '법학관', '복지관', '본부관', '북악관', '예술관', '조형관',
                            '조형관별관', '형설관']
            }
        }
    )
