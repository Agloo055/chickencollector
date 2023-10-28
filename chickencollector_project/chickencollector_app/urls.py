from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chickens/', views.chickens_index, name='index'),
    path('chickens/<int:pk>/', views.chickens_detail, name='detail'),
    path('chickens/create/', views.ChickenCreate.as_view(), name='chickens_create'),
]