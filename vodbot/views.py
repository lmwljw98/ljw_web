import requests
import json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

final_url = []
temp = []
mediaCode_list = []
mediaFre_list = []
base_url = "http://cjpiporigin.myskcdn.com/VOD/"
page = 12


def searchMediaCode(name, page_):
    keyword = name
    mediaCode_list.clear()
    mediaFre_list.clear()
    temp.clear()
    final_url.clear()

    params = {'kwd': keyword, 'pageNum': page_, 'pageSize': 12}
    mediaCode_request = requests.get('http://search.tving.com:8080/search/getFind.jsp', params=params,
                                     proxies={"https": "https://211.58.248.163:3128"})
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
        programCode_request = s.get('https://api.tving.com/v1/media/stream/info', params=second_params,
                                    proxies={"https": "https://211.58.248.163:3128"})
        programCode = json.loads(programCode_request.text)

        realCode = programCode['body']['content']['info']['program']['enm_code']
        fre_number = mediaFre_list[j]

        final_url.append(temp[j] + "\n" + base_url + realCode + "/" + realCode + "_" + fre_number + ".mp4")

    return final_url[page_ - 12: page_]


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
    global page

    if name == '더 보기':
        page += 1
        return JsonResponse(
            {
                'message': {
                    'text':
                        "\n\n".join(searchMediaCode(name, page))
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['더 보기', '다른 키워드로 검색']
                }
            }
        )
    elif name == '다른 키워드로 검색':
        page = 1
        return JsonResponse(

            {
                'type': 'text',
            }
        )
    else:
        page = 1
        return JsonResponse(
            {
                'message': {
                    'text':
                        "\n\n".join(searchMediaCode(name, page))
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['더 보기', '다른 키워드로 검색']
                }
            }
        )
