
from django.urls import path
from .views import index
from django.conf import settings

from django.contrib import admin
from django.urls import path
from .views import file_list , file_upload
urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('list/', file_list),
    #path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('upload/', file_upload, name='file_upload'),
    #path('file/list/create_file/', create_file, name='create_file')
    #path('create_file/', create_file, name='create_file')

    
]




