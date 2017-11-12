from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^naver/$', views.chart, name='naver'),
    url(r'^daum/$', views.daum, name='daum'),
    url(r'^melon/$', views.melon, name='melon'),
    url(r'^$', views.ma_in, name='ma_in'),
]
