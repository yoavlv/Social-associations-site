from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    path("Show_all_words",views.Show_all_words, name ="words-list"),
    path("Search_page",views.Search_word,name="Search-page"),
    path("add_word",views.add_word, name="add-word"),
    path("practice",views.practice, name = "practice"),
    path("search_function", views.search_function, name='search-function'),


]


