import requests
import json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

final_url = []
temp = []
mediaCode_list = []
mediaFre_list = []
base_url = "http://cjpiporigin.myskcdn.com/VOD/"

search = {}


def searchMediaCode(name, page_):
    keyword = name
    mediaCode_list.clear()
    mediaFre_list.clear()
    temp.clear()
    final_url.clear()

    params = {'kwd': keyword, 'pageNum': page_, 'pageSize': 10}
    mediaCode_request = requests.get('http://search.tving.com:8080/search/getFind.jsp', params=params)
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

        try:
            realCode = programCode['body']['content']['info']['program']['enm_code']
            fre_number = mediaFre_list[j]

            final_url.append(temp[j] + "\n" + base_url + realCode + "/" + realCode + "_" + fre_number + ".mp4")

        except:
            final_url.append(temp[j] + "\nLink not found.")
            continue

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

    if name == '더 보기':
        search['page'] += 1
        return JsonResponse(
            {
                'message': {
                    'text': str(search['page']) + "page\n" + "\n\n".join(searchMediaCode(search['name'], search['page']))
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['더 보기', '다시 검색']
                }
            }
        )

    elif name == '다시 검색':
        search['name'] = ''
        search['page'] = 1
        return JsonResponse(
            {
                'message': {
                    'text': '다른 키워드로 다시 검색합니다.'
                },
                'keyboard': {
                    'type': 'text'
                }
            }
        )

    else:
        search['name'] = name
        search['page'] = 1
        return JsonResponse(
            {
                'message': {
                    'text':
                        str(search['page']) + "page\n" + "\n\n".join(searchMediaCode(search['name'], search['page']))
                },
                'keyboard': {
                    'type': 'buttons',
                    'buttons': ['더 보기', '다시 검색']
                }
            }
        )
