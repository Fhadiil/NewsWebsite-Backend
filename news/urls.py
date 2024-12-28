from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('articles/', views.ArticleListCreateView.as_view(), name='articles'),
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('users/', views.UserView.as_view(), name='users'),
    path('articles/<int:pk>/', views.ArticleDetailAPI.as_view(), name='article'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
