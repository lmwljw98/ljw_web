import requests
import json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

mediaCode_list = []
mediaStr_list = []
base_url = "http://cjpiporigin.myskcdn.com/VOD/"


def searchMediaCode(keyword):
    mediaCode_list.clear()
    mediaStr_list.clear()
    params = {'kwd': keyword, 'pageSize': 50}
    mediaCode_request = requests.get('http://search.tving.com:8080/search/getFind.jsp', params=params)
    mediaCode = json.loads(mediaCode_request.text)

    for i in range(len(mediaCode['vodBCRsb']['dataList'])):
        mediaStr_list.append(str(i) + " = " + mediaCode['vodBCRsb']['dataList'][i]['epi_nm'])
        mediaCode_list.append(mediaCode['vodBCRsb']['dataList'][i]['epi_cd'])
    myStr = "\n".join(mediaStr_list)

    return myStr


def searchProgramCode(index):
    k = mediaCode_list[index]
    os.system("python3 ./vodbot/search.py %s &" % k)


def text(request):
    return JsonResponse(
        {
            'type': 'text'
        }
    )


@csrf_exempt
def message(request):
    str = ((request.body).decode('utf-8'))
    received = json.loads(str)
    name = received['content']

    if name.isdigit():
        number = int(name)
        searchProgramCode(number)

        return JsonResponse(
            {
                'message': {
                    'text':
                        "잠시 대기한 뒤(약 5초간) 'ok [보고 싶은 화]'를 입력해주세요.\n\nEX) ok 7 -> 입력 시 7화"
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )
    elif name.split()[0] == "ok":
        f = open("result.txt", "r")
        code = f.readline()
        f.close()

        return JsonResponse(
            {
                'message': {
                    'text': base_url + code + "/" + code + "_" + name.split()[1] + ".mp4"

                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )

    else:
        my = searchMediaCode(name)
        return JsonResponse(
            {
                'message': {
                    'text': my + "\n\n원하는 프로그램의 번호를 입력하세요."

                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )
