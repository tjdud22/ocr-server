"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#static과 media 경로 등록하기위해 import
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

#say_hello 매서드 맵핑
from boards.views import say_hello


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', say_hello), 
    path('api/v1/boards/', include("boards.urls")), 
    #1단계. urls 가없어서 다음 단계로 (urls.py 파일 추가)
    path('api/v1/users/',include("users.urls")),



    #로그인 path 등록 (app등록)
    path('',include("ocr.urls"))

]

#static과 media 경로 등록
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

