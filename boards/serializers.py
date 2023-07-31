from rest_framework.serializers import ModelSerializer 
from .models import Board

from users.serializers import UserOverviewSerializer



 #상속받은 나만의 serializer만들기
class BoardSerializer(ModelSerializer) :
    author = UserOverviewSerializer(read_only=True)




    #정의하는 과정에서 속성값을 담아줘야함
    #속성 답을땐 Meta 지정해주기
    class Meta :
        #model지정하지않으면 serializer 동작 X, json 구조가 없으니까?
        model = Board
        fields = "__all__"

        # depth = 1
        # [
        #  "title",
        #   "content",
         #   "author",
    # ]               
        # exclude = [
        #     "updateAt"
        # ]                     

