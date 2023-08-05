from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from root import settings

urlpatterns = [
                  path('', include('apps.urls')),
                  path('users/', include('users.urls')),
                  path('', include('quiz.urls')),
                  path('admin/', admin.site.urls)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
