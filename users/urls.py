#2단계 

from django.urls import path
from .views import *


urlpatterns = [
    #default path
    path("",Users.as_view()), 
    # 특정유저 타겟팅
    path('user/<int:pk>',UserDetail.as_view()),
    path("list",UserList.as_view()),
    path("login",Login.as_view()),
    path("logout",Logout.as_view()),
    # path("join",join.as_view()),


]


