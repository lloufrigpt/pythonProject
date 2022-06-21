from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pythonProject/', include('pythonProject.urls')),
    path('admin/', admin.site.urls)
]