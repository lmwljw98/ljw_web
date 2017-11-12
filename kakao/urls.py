from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.kakao, name='kakao'),
]