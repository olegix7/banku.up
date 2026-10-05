from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bank/<int:pk>/', views.bank_detail, name='bank_detail'),
]
