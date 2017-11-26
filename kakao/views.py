import codecs
import os
from django.shortcuts import render
from .forms import UploadFileForm


def kakao(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            temp = os.listdir("./mysite/media/")

            f = codecs.open("./mysite/media/" + temp[0], "r", "utf-8")

            line = f.readlines()

            startdate = []

            startdate.append(line[3].replace('-', ''))  # 처음 날짜

            name = []
            dic = {}
            ret_list = []

            first = []

            for i in range(len(line)):

                if line[i].find('[') >= 0 or line[i].find(']') >= 0:
                    name.append(line[i][line[i].find('[') + 1: line[i].find(']')])

            for w in name:
                if w not in dic:
                    dic[w] = 1

                else:
                    dic[w] += 1

            for n in sorted(dic, key=dic.get, reverse=True):
                ret_list.append((n, str(dic[n]) + "번"))

            f.close()
            first.append(ret_list[0][0])

            os.remove("./mysite/media/" + temp[0])

            return render(request, 'kakao/analyze.html', {'list': ret_list, 'one': first, 'start': startdate})

    else:
        form = UploadFileForm()
    return render(request, 'kakao/upload.html', {'form': form})
