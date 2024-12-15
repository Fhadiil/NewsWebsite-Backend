from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='articles'),
    path('articles/<int:pk>/', views.ArticleDetailAPI.as_view(), name='article'),
]