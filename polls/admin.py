from django.contrib import admin

# Register your models here.

from .models import Words




@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    fields =  ('English_word', 'Hebrew_word', 'How_To_Remember',"Name","approved")
    list_display = ('English_word', 'Hebrew_word', 'How_To_Remember',"Name","approved")
    list_editable = ("approved",)
    ordering = ('pub_date',)
    search_fields = ('English_word', 'Hebrew_word')


