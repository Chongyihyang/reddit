from django.conf import *
from django.conf.urls.static import *
from django.contrib import admin
from django.urls import path
from post.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('post/<str:pk>', post_detail),
    path("create", post_create),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)