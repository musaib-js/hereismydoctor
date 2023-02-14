from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header  =  "Admin Panel - Here is my Doctor"  
admin.site.site_title  =  "Here is my Doctor"
admin.site.index_title  =  "Here is my Doctor"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('medicare/', include('hospitals.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)