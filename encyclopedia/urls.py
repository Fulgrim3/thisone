from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("test", views.test, name="test"),
    path("<str:title>", views.title, name="title"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newpage, name="newpage"),
    
    #changed here
    path("editpage/<str:title>", views.edit, name="editpage"),
    path("random/", views.randompage, name="random"),
    #404.html does not need a url path because it is coded into the site
]