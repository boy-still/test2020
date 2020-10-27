from django.urls import path, include
from django.contrib import admin
urlpatterns = [
    path('', include('mqttserver.urls')),
    path('admin/', admin.site.urls),
    path('test/', include('mqttserver.urls'))
]