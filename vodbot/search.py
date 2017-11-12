import requests
import sys, json

mediaCode = sys.argv[1]


def searchProgramCode():
    second_params = {'mediaCode': mediaCode, 'info': 'Y'}
    s = requests.Session()
    programCode_request = s.get('http://api.tving.com/v1/media/stream/info', params=second_params,
                                proxies={'http': 'http://210.101.131.229:8080'})
    programCode = json.loads(programCode_request.text)

    realCode = programCode['body']['content']['info']['program']['enm_code']

    return realCode


code = searchProgramCode()

f = open("result.txt", "w")
f.write(code)
f.close()
