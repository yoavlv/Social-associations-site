from django.urls import path

from . import views

urlpatterns = [
    path("add_hebrew_word", views.add_hebrew_word, name= "add-hebrew-word"),
    path("add_analog", views.add_analog, name= "add-analog"),
    # path("practice_analog", views.practice_analog, name= "practice-analog"),
    path("Show_all_hebrew_words", views.Show_all_hebrew_words, name="Show-all-hebrew-words-list"),
    # path("hebrew-words", views.hebrew_words, name="hebrew-words"),

]

