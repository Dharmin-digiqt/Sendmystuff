from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'', include('main.urls')),
    url(r'', include('blog.urls')),
    url(r'', include('truck_service.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
