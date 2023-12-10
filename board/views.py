from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Board index page.")

# 다음과 같이 수정
from .models import Board
from django.views import generic
from django.urls import reverse_lazy

# 4.1 Board 어플리케이션 - 전체 리스트 조회 기능 작성
def index(request):
    board_main = Board.objects.order_by('-create_date')
    context = {'board_main': board_main}
    return render(request, 'board/board_main.html', context)

class KboView(generic.ListView):
    model = Board
    template_name = 'board/board_kbo.html'
    context_object_name = 'board_main'