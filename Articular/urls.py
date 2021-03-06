from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls')),
    path('', include('apps.blog_detail.urls')),
    path('', include('apps.userProfile.urls')),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)