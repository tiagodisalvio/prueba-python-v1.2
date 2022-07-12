from django.urls import path
from pages import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('', views.pages, name='homePages'),
    path('newPost/', views.newPost, name='newPost'),
    path('postDetail/<pk>', views.PostDetail.as_view(), name = 'postDetail'),
    path('postDelete/<pk>', views.PostDelete.as_view(), name = 'postDelete'),
    path('postUpdate/<post_id>/',views.postUpdate, name = "postUpdate"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()