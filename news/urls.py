from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='articles'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('users/', views.UserView.as_view(), name='users'),
    path('articles/<int:pk>/', views.ArticleDetailAPI.as_view(), name='article'),
]