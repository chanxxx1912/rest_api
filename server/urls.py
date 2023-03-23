
from django.urls import path
from .views import index
from django.conf import settings

from django.contrib import admin
from django.urls import path
from .views import file_list ,file_create
urlpatterns = [
    path('', index, name='index'),
    #path('admin/', admin.site.urls),
    path('list/', file_list),
    path('post/', file_create),
    
]




