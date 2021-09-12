
from .models import Words
from django import forms
from django.forms import ModelForm
import random

from datetime import time

from django.utils import timezone


class WordForm(ModelForm):
    class Meta:
        model = Words
        fields = ('English_word', 'Hebrew_word', 'How_To_Remember', 'Name')
        labels = {
            'English_word': '',
            'Hebrew_word': '',
            'How_To_Remember': '',
            'Name': '',

        }
        widgets = {
            'English_word': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'איזו מילה תרצה להכניס למאגר?'}),
            'Hebrew_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '?מה הפירוש למילה'}),
            'How_To_Remember': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'מה האסוציאציה שחשבת עליה?'}),
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מה השם שלך?'}), }

#
# class QuizFrom(forms.Form):
#
#
#     def makequiz(self):
#         words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
#         random_word_to_guess = random.choice(words_list) # Take one random words from the DB
#         x = random_word_to_guess.English_word
#         word_1 = random.choice(words_list)
#         word_2 = random.choice(words_list)
#         word_3 = random.choice(words_list)
#         # OPTIONS = (("1",word_1.Hebrew_word),("2", word_2.Hebrew_word), ("3",word_3.Hebrew_word), (4,random_word_to_guess.Hebrew_word))
#         quiz_list = [word_1.Hebrew_word, word_2.Hebrew_word, word_3.Hebrew_word, random_word_to_guess.Hebrew_word]
#
#         option_0 = forms.BooleanField(label=quiz_list[0],required=False,initial=False)
#         option_1 = forms.BooleanField(label=quiz_list[1],required=False,initial=False)
#         option_2 = forms.BooleanField(label=quiz_list[2],required=False,initial=False)
#         option_3 = forms.BooleanField(label=quiz_list[3],required=False,initial=False)
#
#         all_options = [option_1,option_2,option_3,option_0]
#
#         # choice_field = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
        # option_0 = forms.BooleanField(widget=forms.TextInput(attrs={"name":"quiz",'class':'btn btn-primary','type':"submit","id":"option-1",'value':quiz_list[0]}))
        # option_1 = forms.BooleanField(widget=forms.TextInput(attrs={"name":"quiz",'class':'btn btn-primary','type':"submit","id":"option-1",'value':quiz_list[1]}))

# def makequiz(self):
#     words_list = Words.objects.filter(approved= True)  # Take all the words that approved by the admin
#     random_word_to_guess = random.choice(words_list) # Take one random words from the DB
#     x = random_word_to_guess.English_word
#     word_1 = random.choice(words_list)
#     word_2 = random.choice(words_list)
#     word_3 = random.choice(words_list)
#     # OPTIONS = (("1",word_1.Hebrew_word),("2", word_2.Hebrew_word), ("3",word_3.Hebrew_word), (4,random_word_to_guess.Hebrew_word))
#     quiz_list = [word_1.Hebrew_word, word_2.Hebrew_word, word_3.Hebrew_word, random_word_to_guess.Hebrew_word]
#
#     option_0 = forms.BooleanField(widget=forms.TextInput(attrs={"name":"quiz",'class':'btn btn-primary','type':"submit","id":"option-1",'value':quiz_list[0]}))
#     option_1 = forms.BooleanField(widget=forms.TextInput(attrs={"name": "quiz", 'class': 'btn btn-primary', 'type': "submit", "id": "option-1", 'value': quiz_list[1]}))
#
#
#         # choice_field = forms.ChoiceField(widget=forms.Select, choices=OPTIONS)
#         # option_0 = forms.BooleanField(widget=forms.TextInput(attrs={"name":"quiz",'class':'btn btn-primary','type':"submit","id":"option-1",'value':quiz_list[0]}))
#         # option_1 = forms.BooleanField(widget=forms.TextInput(attrs={"name":"quiz",'class':'btn btn-primary','type':"submit","id":"option-1",'value':quiz_list[1]}))
