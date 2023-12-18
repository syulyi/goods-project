from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

# def index(request):
#     return HttpResponse("Board index page.")

# 다음과 같이 수정
from .models import Board
from django.views import generic
from django.urls import reverse_lazy
from .models import Product
from .forms import CompareProductForm

# 4.1 Board 어플리케이션 - 전체 리스트 조회 기능 작성
def index(request):
    board_main = Board.objects.order_by('-create_date')
    context = {'board_main': board_main}
    return render(request, 'board/board_main.html', context)

# def FanBoard(request):
#     board_fan = Board.objects.order_by('-create_date')
#     context = {'board_fan': board_fan}
#     template_name = 'board/board_fan.html'
#     context_object_name = 'board_fan'
#     return render(request, 'board/board_fan.html', context)

class FanBoard(generic.ListView):
    # model = Board
    template_name = 'board/board_fan.html'
    context_object_name = 'board_fan'
    def get_queryset(self):
        return Board.objects.order_by('-create_date')


def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'board/board_fan_detail.html', context)

class create(generic.CreateView):
    model = Board
    fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy('board:fan')
    template_name_suffix = '_fan_create'
    # template_name = 'board/board_fan_create.html'
    # def get_success_url(self):
    #     return reverse('board:detail', kwargs={'board_id': self.object.id})

class delete(generic.DeleteView):
    model = Board
    # fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy('board:fan')
    template_name_suffix = '_delete'

class update(generic.UpdateView):
    model = Board
    fields = ['subject', 'content', 'create_date']
    success_url = reverse_lazy('board:fan')
    template_name_suffix = '_form'
    # form_class = YourForm


# KBO 삼성
class KboView(generic.ListView):
    model = Board
    template_name = 'board/board_kbo.html'
    context_object_name = 'board_main'

class KboSamsung(generic.ListView):
    model = Board
    template_name = 'board/board_kbo_samsung.html'
    context_object_name = 'board_samsung'

class SamsungProd001(generic.ListView):
    model = Board
    template_name = 'board/board_kbo_samsung_001.html'
    context_object_name = 'board_prod'

# KBO 엔씨
class KboNc(generic.ListView):
    model = Board
    template_name = 'board/board_kbo_nc.html'
    context_object_name = 'board_nc'

class NcProd001(generic.ListView):
    model = Board
    template_name = 'board/board_kbo_nc_001.html'
    context_object_name = 'board_prod'

def compare_product(request):
    products = Product.objects.all()
    form = CompareProductForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        product1_id = form.cleaned_data['product1']
        product2_id = form.cleaned_data['product2']

        # 선택한 ID를 기반으로 상품 이름을 가져옵니다
        selected_product_1 = Product.objects.get(id=product1_id).name
        selected_product_2 = Product.objects.get(id=product2_id).name

        # 필요한 경우 추가적인 비교 로직을 수행합니다

        return render(request, 'board/compare_product.html', {
            'products': products,
            'form': form,
            'selected_product_1': selected_product_1,
            'selected_product_2': selected_product_2,
        })


    # return render(request, 'board/compare_product_form.html', {'form': form})
    return render(request, 'board/compare_product.html', {'products': products, 'form': form})

def kbo_sm_prod_001_view(request):
    return render(request, 'board/kbo_sm_prod_001.html')