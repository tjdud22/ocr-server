from rest_framework.decorators import api_view
#응답을 위해 추가
from rest_framework.response import Response
#APIView 활용
from rest_framework.views import APIView
#try-catch추가하기위해 추가
from rest_framework.exceptions import NotFound,PermissionDenied

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import render
#사용자에게 보여질? response 핸들링 작성하기

from django.http.response import HttpResponse

import users
from .models import Board
from .serializers import BoardSerializer

from django.shortcuts import redirect

#추가
from pyuploadcare import Uploadcare, File
from django.conf import settings



def say_hello(request) :
    return render(request, "index.html", {
        "data" : Board.objects.all()
    }) 


# @api_view(['GET', 'POST'])
# def get_board_all(request) :
#     boards = Board.objects.all()
#     # -> Board를 JSON으로 형변환 (Serializer)
#     serializer = BoardSerializer(boards, many=True)
#     return Response(serializer.data)


#decorate 안쓰려고 APIView 사용
#servlet 생김새와 유사
class Boards(APIView) : 

    permission_classes = [IsAuthenticatedOrReadOnly] #post버튼 없어짐, 인증된 사용자가 아니면 readonly save메서드를 제외하고 나머지 제한



    def get(self, request) : 
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response(serializer.data) #json string 가져옴

    def post(self,request) :
        #유효성 검사 후 save 처리 가능
        #print(request.data)
        #새로운 data로 들어감, data 속성 명시 후 request.data 대입
        serializer = BoardSerializer(data=request.data)

            #유효성 검사후 t/f 반환
        if serializer.is_valid() :
            board = serializer.save() # create() 메소드를 호출하게 됨 

# 게시글존재&& 파일크기제한 발급받은 키를 활용해서 생성 upload메서드 활용해서 100mb 이하 파일 업로드
            if board.loaded_file and board.loaded_file.size < settings.FILE_SIZE_LIMIT :
                uploadcare = Uploadcare(public_key=settings.UC_PUBLIC_KEY, secret_key=settings.UC_SECRET_KEY)
                with open(board.loaded_file.path, 'rb') as file_object:
                    ucare_file = uploadcare.upload(file_object)
                    image_url = f"https://ucarecdn.com/{ucare_file.uuid}/"
                    board.image_url = image_url



            board.author = request.user
            board.save()
            return redirect(f'/board/{board.pk}')
            # serializer.save() # 내장되어있는 create() 메소드를 호출하게 됨 
            # return Response(serializer.data) 
        return Response(serializer.errors)

    # def delete() :
    #     pass


class BoardDetail(APIView) :

    #인증된 사용자 + author = request.user

    permission_classes = [IsAuthenticatedOrReadOnly]
   

    def get_object(self,pk) :

        
        try :
            board = Board.objects.get(pk=pk)
            return board
        except Board.DoesNotExist :
            raise NotFound   
        
    def get(self, request,pk) :
            #pk를 가져와서 -> 보드 한개 가져오기
            board = self.get_object(pk)
            #보드 인스턴스를 -> JSON 형변환
            serializer = BoardSerializer(board)
            #Response 객체로 반환 
            return Response(serializer.data)

    def put(self, request,pk) :
        
        board = self.get_object(pk)

        if not board.author == request.user :
            raise PermissionDenied

        serializer = BoardSerializer(instance=board, data=request.data,partial=True)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def delete(self, request, pk) :
        board = self.get_object(pk)

        if not board.author == request.user : 
            raise PermissionDenied

        board.delete()
        return Response({})

    # def delete(self, request,pk) :
         
    #     if not board.author == request.user :
    #         raise PermissionDenied
      
        
    #     board = self.get_object(pk)
    #     board.delete()
    #     return Response({})



# @api_view(['GET', 'POST'])
# def get_board_all(request) :
#     boards = Board.objects.all()
#     # -> Board를 JSON으로 형변환 (Serializer)
#     serializer = BoardSerializer(boards,many=True)

#     return Response(
#         # "data" : serializer.data
#         serializer.data
#     )

    
    
     #요청값 들고 index.html 페이지로 response 처리
#java에서는 setattribute , get 
# data 값이 존재하면 화면에 뿌려줌~
# jstl <% 처럼 

# board의 전체 object를 반환해주는 메서드 작성 , restful api에 맞춰 구현해주기 위해 rest framework import
#rest 요청을 처리해줄거라는걸 명시
# @api_view(['GET','POST'])
# def get_board_all(request):
    #board 전체값 가져오기
    # boards = Board.objects.all()
#->model ㅠJSON으로 형변환(Serializer 활용,정의해야 사용가능)

    #응답처리 위한 개체 만들기
    # return Response({
#딕셔너리로 담긴 데이터를 반환? json타입으로 반환
        # "status" : "OK"
        # "data" : boards 
        # #오류:Object of type Board is not JSON serializable
    # })