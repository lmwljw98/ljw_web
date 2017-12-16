import requests
import json, os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

final_url = []
base_url = "http://cjpiporigin.myskcdn.com/VOD/"

proxies = {
    "https": "https://211.58.248.163:3128"
}


def searchMediaCode(name):
    try:
        keyword = name
        final_url.clear()

        params = {'kwd': keyword, 'pageSize': 1000}
        mediaCode_request = requests.get('http://search.tving.com:8080/search/getFind.jsp', params=params,
                                         proxies=proxies)
        mediaCode = json.loads(mediaCode_request.text)

        for i in range(len(mediaCode['vodBCRsb']['dataList'])):

            second_params = {'mediaCode': mediaCode['vodBCRsb']['dataList'][i]['epi_cd'], 'info': 'Y'}
            programCode_request = requests.get('http://api.tving.com/v1/media/stream/info', params=second_params,
                                               proxies=proxies)
            programCode = json.loads(programCode_request.text)

            realCode = programCode['body']['content']['info']['program']['enm_code']
            fre_number = mediaCode['vodBCRsb']['dataList'][i]['frequency']

            final_url.append(mediaCode['vodBCRsb']['dataList'][i]['mast_nm'].replace("#@$", "").replace("$#@", "") + " "
                + mediaCode['vodBCRsb']['dataList'][i]['frequency'] + "화\n" + base_url + realCode + "/" + realCode +
                             "_" + fre_number + ".mp4")

    except:
        return "Error"


@csrf_exempt
def message(request):
    user_request = ((request.body).decode('utf-8'))
    received = json.loads(user_request)
    name = received['content']

    searchMediaCode(name)

    return JsonResponse(
        {
            'message': {
                'text':
                    "\n".join(final_url)
            },
            'keyboard': {
                'type': 'text'
            }
        }
    )
