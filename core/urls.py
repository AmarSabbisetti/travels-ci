
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/',include(('users.urls','users'),namespace='users')),
    path('api/packages/',include(('packages.urls','packages'),namespace='packages')),
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)