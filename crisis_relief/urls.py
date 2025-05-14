# crisis_relief/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('affected/', include('Affected.urls')),
    path('task/', include('Task.urls')),
]
