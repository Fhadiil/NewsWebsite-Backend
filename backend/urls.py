from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.core.management import call_command
from django.conf.urls.static import static
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),
    path('create-superuser/', lambda request: (call_command('createsuperuser'), HttpResponse('Superuser created.'))),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)