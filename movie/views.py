from django.shortcuts import render
from .models import *
from .forms import Tform

# Create your views here.


code_dict = {'프로듀스 101' : 'B120156957', '프로듀스 101 비하인드' : 'B120160158', '스탠바이 아이오아이' : 'B120169905',
             'SNL KOREA 시즌7' : 'B120169319', '현장토크쇼 TAXI' : 'B120121205', '신서유기3' : 'B120162397',
             '도깨비' : 'B120161931', '삼시세끼 어촌편 1' : 'B120144786', '삼시세끼 어촌편 2' : 'B120157939',
             '고등래퍼' : 'B120161933', '인생술집' : 'B120162400', '더 지니어스2' : 'B120130827', '더 지니어스3' : 'B120143351',
             '더 지니어스4' : 'B120156585', '윤식당' : 'B120163290', 'DDL' :
             'B120174231','신서유기4' : 'B120174658', '구해줘' : 'B120174785'
             }

common_url = 'http://cjpiporigin.myskcdn.com/VOD/'

def movie(request):

    if Lock.objects.filter(lock="on"):

        Tv_choice.objects.all().delete()
        Output.objects.all().delete()

        form = Tform(request.POST)

        if form.is_valid():

            my_code = form.save()

            if "GO" in request.POST:

                Tv_choice.objects.all().delete()
                Output.objects.all().delete()

                if my_code.tv == 'produce101':

                    tv_code = code_dict['프로듀스 101']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'behind':

                    tv_code = code_dict['프로듀스 101 비하인드']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'standby':

                    tv_code = code_dict['스탠바이 아이오아이']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'snl':

                    tv_code = code_dict['SNL KOREA 시즌7']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'taxi':

                    tv_code = code_dict['현장토크쇼 TAXI']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'sin3':

                    tv_code = code_dict['신서유기3']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'sin4':

                    tv_code = code_dict['신서유기4']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'goblin':

                    tv_code = code_dict['도깨비']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'food3_sea_1':

                    tv_code = code_dict['삼시세끼 어촌편 1']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'food3_sea_2':

                    tv_code = code_dict['삼시세끼 어촌편 2']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'high_rap':

                    tv_code = code_dict['고등래퍼']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'life_':

                    tv_code = code_dict['인생술집']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'genious_2':

                    tv_code = code_dict['더 지니어스2']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'genious_3':

                    tv_code = code_dict['더 지니어스3']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()

                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'genious_4':

                    tv_code = code_dict['더 지니어스4']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()
                    
                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'yoon':

                    tv_code = code_dict['윤식당']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()
                    
                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})


                elif my_code.tv == 'ddl':

                    tv_code = code_dict['DDL']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()
                    
                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})

                elif my_code.tv == 'rngownj':

                    tv_code = code_dict['구해줘']

                    t = Output(src=common_url + tv_code + '/' + tv_code + '_' + my_code.num + '.mp4')
                    t.save()
                    
                    return render(request, 'movie/movie.html', {'source': Output.objects.all(), 'form': form})
 
                else:

                    return render(request, 'movie/lock.html')  # 출력
        else:

            form = Tform()
            return render(request, 'movie/movie.html', {'form': form})

    else:

        return render(request, 'movie/lock.html')   # 출력
