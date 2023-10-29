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

      # All Snacks URLs
    path('snacks/', views.SnackList.as_view(), name='snacks_index'),
    path('snacks/<int:pk>/', views.SnackDetail.as_view(), name='snacks_detail'),
    path('snacks/create/', views.SnackCreate.as_view(), name='snacks_create'),
    path('snacks/<int:pk>/update/', views.SnackUpdate.as_view(), name='snacks_update'),
    path('snacks/<int:pk>/delete/', views.SnackDelete.as_view(), name='snacks_delete'),
]