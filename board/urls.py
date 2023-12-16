from django.urls import path

from . import views
from .views import compare_products

app_name = "board"

urlpatterns = [
    path('', views.index, name = 'main'),
    path('kbo/', views.KboView.as_view(), name='kbo'),
    path('kbo/samsung/', views.KboSamsung.as_view(), name='samsung'),
    path('kbo/samsung/prod/', views.SamsungProd001.as_view(), name='prod001'),
    path('compare/', compare_products, name='compare_products'),
]