from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('', views.list_files, name='list_files'),
    path('upload/', views.upload_file, name='upload_file'),
]
