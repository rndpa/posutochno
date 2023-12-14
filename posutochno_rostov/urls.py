from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from posutochno_rostov import settings

from posutochno.views import *
from users.views import *

from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('posutochno.urls')),
    path('снять-квартиру-посуточно/', include('posutochno.urls')),
    path('снять-дом-посуточно/', include('house.urls')),
    path('снять-отель-посуточно/', include('hotels.urls')),
    path('пользователь/', include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
