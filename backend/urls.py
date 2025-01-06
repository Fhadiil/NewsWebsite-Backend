from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.core.management import call_command
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def create_superuser_view(request):
    User = get_user_model()  # Get the custom user model
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username='admin', 
            email='fadeelaliyu51@example.com', 
            password='admin77@',
            is_journalist=True
        )
        return HttpResponse("Superuser created successfully!")
    else:
        return HttpResponse("Superuser already exists.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),
    path('create-superuser/', create_superuser_view),
]

if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)