from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.notebooks, name="home"),
    path("home", views.notebooks),
    path("notebooks", views.notebooks, name="notebooks"),
    path("notebooks/<int:id>", views.details, name="details"),
    path("maxprice", views.maxprice, name="maxprice"),
    path("minprice", views.minprice, name="minprice"),
    path("search", views.search, name="search"),
    

]