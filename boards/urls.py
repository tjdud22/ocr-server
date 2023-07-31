from django.urls import path
# from .views import get_board_all
from .views import *

# urlpatterns = [
#     path('', get_board_all),
#     path('board', get_board_all),#admin path 표방
# ]

urlpatterns = [
    path('', Boards.as_view()),
   path('board/<int:pk>',BoardDetail.as_view()),#<int:>형식
]

 