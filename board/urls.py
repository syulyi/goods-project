from django.urls import path

from . import views
from .views import compare_product

app_name = "board"

urlpatterns = [
    path('', views.index, name='main'),
    path('kbo/', views.KboView.as_view(), name='kbo'),
    path('kbo/samsung/', views.KboSamsung.as_view(), name='samsung'),
    path('kbo/samsung/prod/', views.SamsungProd001.as_view(), name='prod001'),
    path('compare/', compare_product, name='compare_products'),
    path('kbo/samsung/prod001/', views.kbo_sm_prod_001_view, name='kbo_sm_prod_001'),
    # path('', views.index, name='fan'),
    path('fan/', views.FanBoard.as_view(), name='fan'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('fan/create/', views.create.as_view(), name='create_fan'),
    # path('create/', views.create.as_view(), name='create'),
    path('<int:pk>/delete/', views.delete.as_view(), name='delete'),
    path('<int:pk>/update/', views.update.as_view(), name='update'),
]