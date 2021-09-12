from django.contrib import admin
from .models import  hebrew_words , Analog

# Register your models here.
@admin.register(hebrew_words)
class hebrew_wordsAdmin(admin.ModelAdmin):
    fields =  ('word', 'meaning', 'Sentence',"pub_date","approved")
    list_display = ('word', 'meaning', 'Sentence',"pub_date","approved")
    list_editable = ('meaning', 'Sentence',"pub_date","approved",)
    ordering = ('pub_date',)
    search_fields = ('word', 'meaning')

@admin.register(Analog)
class AnalogAdmin(admin.ModelAdmin):
    fields =  ('First_word', 'Second_word',"Third_word" ,"Fourth_word","Sentence","Difficulty","pub_date","approved")
    list_display = ('First_word', 'Second_word',"Third_word" ,"Fourth_word","Sentence","Difficulty","pub_date","approved")
    list_editable = ("approved",)
    ordering = ('pub_date',)
    search_fields = ('First_word', 'Second_word',"Third_word" ,"Fourth_word" )

