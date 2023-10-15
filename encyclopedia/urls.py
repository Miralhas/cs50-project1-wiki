from django.urls import path
from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"), # wiki:index
    path("wiki/<str:title>/", views.wiki_page, name="wiki_page"), # wiki:wiki_page
    path("search/", views.search, name="search"), # wiki:search
    path("new_wiki/", views.add_wiki, name="add_wiki"), #wiki:add_wiki
    path("update_wiki/<str:title>/", views.update_wiki, name="update_wiki"), #wiki:update_wiki
    path("random/", views.random_wiki, name="random") #wiki:random
]
