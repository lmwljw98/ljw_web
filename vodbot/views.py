import requests
import json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

final_url = []
temp = []
mediaCode_list = []
mediaFre_list = []
base_url = "http://cjpiporigin.myskcdn.com/VOD/"


def searchMediaCode(name):
    keyword = name
    mediaCode_list.clear()
    mediaFre_list.clear()
    temp.clear()

    params = {'kwd': keyword, 'pageSize': 50}
    mediaCode_request = requests.get('http://search.tving.com:8080/search/getFind.jsp', params=params,
                                     proxies=proxies)
    mediaCode = json.loads(mediaCode_request.text)

    for i in range(len(mediaCode['vodBCRsb']['dataList'])):
        temp.append(
            mediaCode['vodBCRsb']['dataList'][i]['mast_nm'].replace("#@$", "").replace("$#@", "") + " "
            + mediaCode['vodBCRsb']['dataList'][i]['frequency'] + "화")
        mediaCode_list.append(mediaCode['vodBCRsb']['dataList'][i]['epi_cd'])
        mediaFre_list.append(mediaCode['vodBCRsb']['dataList'][i]['frequency'])

    for j in range(len(mediaCode_list)):
        second_params = {'mediaCode': mediaCode_list[j], 'info': 'Y'}
        s = requests.Session()
        programCode_request = s.get('http://api.tving.com/v1/media/stream/info', params=second_params,
                                    proxies={"http": "http://14.52.23.216:8080"})
        programCode = json.loads(programCode_request.text)

        realCode = programCode['body']['content']['info']['program']['enm_code']
        fre_number = mediaFre_list[j]

        final_url.append(temp[i] + "\n" + base_url + realCode + "/" + realCode + "_" + fre_number + ".mp4")

    return final_url


def text(request):
    return JsonResponse(

        {
            'type': 'text',

        }
    )


@csrf_exempt
def message(request):
    user_request = ((request.body).decode('utf-8'))
    received = json.loads(user_request)
    name = received['content']

    return JsonResponse(
        {
            'message': {
                'text':
                    "\n\n".join(searchMediaCode(name))
            },
            'keyboard': {
                'type': 'text'
            }
        }
    )
