from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='articles'),
    path('articles/<str:category_name>/', views.ArticleByCategoryView.as_view(), name='articles_by_category'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('users/', views.UserView.as_view(), name='users'),
    path('articles/<int:pk>/', views.ArticleDetailAPI.as_view(), name='article'),
]
