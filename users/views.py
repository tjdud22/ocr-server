#3단계
#유저정보 전체 조회하기 위해서는 usermodel 필요. (model 패키지 안에있음 >from .models import User 로 가져오기)

from .models import User
from rest_framework.views import APIView
#serializers 만들고 사용하기
from .serializers import UserSerializer, UserViewSerializer 
from rest_framework.response import Response
#NotFound > rest_framework가 제공해줌
from rest_framework.exceptions import NotFound,PermissionDenied
from django.http.response import HttpResponse

# from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework import status

from rest_framework.permissions import IsAuthenticated


#로그인,로그아웃 메서드
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


from .serializers import *

#로그인 추가
class Login(APIView) :
    def post(self,request) :
        username = request.data.get("username")
        password = request.data.get("password")

#기존에 가지고 있는 유저정보와 비교하여 인가내릴수있는 메서드 만들기
        user = authenticate(request,username=username, password=password)

        #user인증 확인되면 로그인
        #Not None
        if user : 
            login(request,user)
            return Response({"login" : "success"})
        else :
            return Response(status.HTTP_401_UNAUTHORIZED)


class Logout(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self,request) :
       logout(request)
       return redirect("/api/v1/boards")





class UserList(APIView) :

    permission_classes = [IsAuthenticated]

    def get(self,request) :
        if request.user.is_staff :
            users = User.objects.all()
            serializer = UserSerializer(instance=users , many=True)
            return Response(serializer.data)
        else : 
            raise PermissionDenied

#받은 data를  User class 를 통해서 get,post 해주는것?
#User class는 유효성 검사후 get, post를 처리.
#기본기능?





#APIView 상속받도록 처리 
class Users(APIView) : 
    #정의부
    # def get(self, request) : 

       
    #     #User의 모든 정보를 받아서 users에 담아줌
    #     users = User.objects.all()
    #     #리턴해주기위해서는 serializer을 만들어서 (#4단계)
    #     #json형식으로 변환
    #     #default 인자는 instance= > 생략가능 . 그냥 users로만 써도됨.(users,many=True)
    #     serializer = UserSerializer(instance=users , many=True)
    #     #json 형식으로 처리
    #     #response객체를 serializer로 만들어주기
    #     return Response(serializer.data)

    def post(self,request) :
        #data를request.data로 넘겨서 유효성검사 ()
        serializer = UserSerializer(data=request.data)
        #is_valid 메서드로 유효성 검사 후 save 처리 
        if serializer.is_valid() :
            user = serializer.save() #유저저장
            #저장한 인스턴스 반환받으면
            #set_password 가 pw를 해싱처리
            print("비번 : ",user.password)
            user.set_password(user.password) #현재 user 가 갖고있는 pw 인자로 넘기면 해싱해줄수있음.저장도.
            user.save()
            #저장성공시
            return Response(UserViewSerializer(user).data)
        #저장실패시 오류사항 내역 출력
        return Response(serializer.errors)
    
    def delete() :
        pass
    


class UserDetail(APIView) :
    permission_classes = [IsAuthenticated]


    #유효성 검사
    def get_object(self,request,pk) : 
        try :
            user = User.objects.get(pk=pk)


        #로그인 되어있어도 유저가 아니면 PermissionDenied 뜸
            if not user == request.user : 
                raise PermissionDenied


            return user
        except User.DoesNotExist :
            raise NotFound 
        #return이면 NotFound 객체로 반환할수없음 ,raise 로 써주기!!

#pk값을 받아서 처리를 할 메서드 열거
#유저 한명 조회
    def get(self,request,pk) :
        #pk를 통해 유저 한명 조회하기
        user = self.get_object(request,pk)
        #유저 인스턴스를 Json 형변환

        serializer = UserViewSerializer(user)
        #Response 객체로 반환
        #many 옵션은 default false > 생략.
        return Response(serializer.data)

#유저수정
    def put(self,request,pk) : 
        user = self.get_object(request,pk)
        serializer = UserSerializer(instance=user,data=request.data,partial=True)

        if serializer.is_valid() : 
            user = serializer.save()

            if 'password' in request.data :
                user.set_password(user.password)
                user.save()

            return Response(serializer.data)
        else :
            return Response(serializer.errors)

#유저삭제
    def delete(self,request,pk) :
        user = self.get_object(request,pk)
        user.delete()
        return Response(status.HTTP_204_NO_CONTENT)          

#직접 추가한 유저의 pw는 해싱이안됨.









#로그인 & 게시판=============================


# from django.shortcuts import render, redirect
# from .models import Board
# from .serializers import BoardSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly

# #게시판

# @api_view(['GET', 'POST'])
# def create_board(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         content = request.POST.get('content')

#         # 유효성 검사 후 Board 객체 생성
#         serializer = BoardSerializer(data={'title': title, 'content': content})
#         if serializer.is_valid():
#             serializer.save(author=request.user)  # 현재 로그인된 사용자를 작성자로 저장
#             return redirect('board_list')  # 게시판 목록 페이지로 리다이렉트
#         else:
#             # 유효성 검사 실패 시 에러 메시지 표시
#             errors = serializer.errors
#             return render(request, 'board_form.html', {'errors': errors})

#     return render(request, 'board_form.html')



# # 로그인 views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login

# def login_view(request):
#     if request.method == 'POST':
#         user_id = request.POST.get('id')
#         user_pwd = request.POST.get('pwd')

#         # 사용자 인증
#         user = authenticate(request, user_id=user_id, user_pwd=user_pwd)

#         if user is not None:
#             # 인증에 성공한 경우 로그인 처리
#             login(request, user)
#             return redirect('index.html')  # 로그인 성공 후 이동할 페이지 설정

#         else:
#             # 인증에 실패한 경우 에러 메시지를 전달하고 로그인 페이지 다시 보여줌
#             return render(request, 'login_form.html', {'error': '아이디 또는 비밀번호가 잘못되었습니다.'})

#     return render(request, 'login_form.html')