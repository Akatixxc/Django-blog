from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts-list'),
    path('create/', views.posts_create, name='posts-create'),
    path('<slug>/update/', views.posts_update, name='posts-update'),
    path('<slug>/delete/', views.posts_delete, name='posts-delete'),
    path('<slug>/', views.posts_detail, name='posts-detail'),
]