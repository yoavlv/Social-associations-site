

from django import forms
from django.forms import ModelForm
from .models import Analog, hebrew_words







class CreateAnalog(ModelForm):
    class Meta:
        model = Analog
        fields = ('First_word', 'Second_word',"Third_word","Fourth_word", 'Sentence', 'Difficulty')
        labels = {
            'First_word': '',
            'Second_word': '',
            'Third_word': '',
            'Fourth_word': '',
            'Difficulty': '',
            'Sentence': '',

        }
        widgets = {
            'First_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מה המילה הרשונה?'}),
            'Second_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '?מה הפירוש למילה?'}),
            'Third_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מה המילה השנייה עם אותה המשמעות?'}),
            'Fourth_word': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מה הפירוש למילה?'}),

            'Sentence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מה המשפט המקשר?'}),
            'Difficulty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'מה רמת הקושי? (1-5)'}), }


class CreateWord(ModelForm):
    class Meta:
        model = hebrew_words
        fields = ('word', 'meaning', 'Sentence')
        labels = {
            'word': '',
            'meaning': '',
            'Sentence': '',

        }
        widgets = {
            'word': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'איזו מילה תרצה להכניס למאגר?'}),
            'meaning': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '?מה משמעות המילה'}),
            'Sentence': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'משפט עם המילה'}), }
