from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chickens/', views.chickens_index, name='index'),
    path('chickens/<int:pk>/', views.chickens_detail, name='detail'),
    path('chickens/<int:pk>/add_laying', views.add_laying, name='add_laying'),

    path('chickens/create/', views.ChickenCreate.as_view(), name='chickens_create'),
    path('chickens/<int:pk>/update', views.ChickenUpdate.as_view(), name='chickens_update'),
    path('chickens/<int:pk>/delete', views.ChickenDelete.as_view(), name='chickens_delete'),
]