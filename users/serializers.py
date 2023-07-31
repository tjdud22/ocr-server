#4단계.

from rest_framework.serializers import ModelSerializer 
from .models import User



class UserSerializer(ModelSerializer) :
    class Meta : 
        model = User 
        fields = "__all__"

class UserViewSerializer(ModelSerializer) :
    class Meta :
        model = User
        fields = [
            "username",
            "name",
            "email",
            "date_joined",
        ]

class UserOverviewSerializer(ModelSerializer) :
    class Meta : 
        model = User 
        fields = [
            "username",
            "name",
        ]









#ModelSerializer 상속받음, 
# 상속받기 위해선 속성정보를 줘야하는데 그 속성정보는 model과 field
#속성정보(model,field) 정의해주기 

#전체 데이터 조회
# class UserSerializer(ModelSerializer) : 
#     class Meta : 
#         model = User
#         fields = "__all__"



# class UserSerializer(ModelSerializer) : 
#     class Meta : 
#         model = User
#         fields = "__all__"




# class UserViewSerializer(ModelSerializer) : 
#     class Meta : 
#         model = User
#         fields = [
#             "username",
#             "name",
#             "email",
#             "date_joined",

#                     ]
       


        

#일부 데이터 조회
class UserOverviewSerializer(ModelSerializer) :
    class Meta :
        model = User
        fields = [
            "username",
            "name",

        ]
