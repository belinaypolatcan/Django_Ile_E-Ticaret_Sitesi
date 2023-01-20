from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include


# http://127.0.0.1:8000/

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainproject.urls'))
]