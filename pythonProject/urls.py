from django.urls import path
from . import views

app_name = 'pythonProject'

urlpatterns = [
    path('', views.index, name='index')
]