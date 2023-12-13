from django.urls import path

from . import views

app_name = "board"

urlpatterns = [
    path('', views.index, name = 'main'),
    path('kbo/', views.KboView.as_view(), name='kbo'),
    path('kbo/samsung/', views.KboSamsung.as_view(), name='samsung'),
    path('kbo/samsung/prod/', views.SamsungProd001.as_view(), name='prod001')
]