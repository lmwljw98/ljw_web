"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from kmucafe.views import keyboard, answer, crawl
from kmuRoom import views
import luda.views
from vodbot import views as vod
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^movie/', include('movie.urls')),
    url(r'^photo/', include('photo.urls')),
    url(r'^capture/', include('capture.urls')),
    url(r'^chart/naver', include('chart.urls')),
    url(r'^chart/daum', include('chart.urls')),
    url(r'^chart/melon', include('chart.urls')),
    url(r'^chart/', include('chart.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^kakao/', include('kakao.urls')),
    url(r'^', include('index.urls')),
    url(r'^geoip/', include('geoip.urls')),
    url(r'^keyboard/', keyboard, name='keyboard'),
    url(r'^message', answer, name='answer'),
    url(r'^crawl/', crawl, name='crawl'),
    url(r'^kmuRoom/keyboard/', views.keyboard, name='keyboard'),
    url(r'^kmuRoom/message', views.answer, name='answer'),
    url(r'^vod/keyboard/', vod.text, name='text'),
    url(r'^vod/message', vod.message, name='message'),
    url(r'^luda/', include('luda.urls')),
    url(r'^luda/db', include('luda.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
