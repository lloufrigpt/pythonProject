from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'pythonProject'

urlpatterns = [
    path('', views.index, name='index'),
]

from django.views.static import serve

url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),