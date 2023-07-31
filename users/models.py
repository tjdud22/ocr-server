from django.db import models
from django.contrib.auth.models import AbstractUser

#class Board(models.Model) :
#    pass


# 장고모델 활용해서 User모델 만들기
class User(AbstractUser) :
    # CharField : 컬럼타입지정
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)

    # 나만의 필드 추가 
    name = models.CharField(max_length=200,default="", blank=True )

    #모델 변경 후 db에게 알려주기 python manage.py makemigrations ,  python manage.py migrate 


