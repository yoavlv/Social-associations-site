from django import forms
from django.forms import ModelForm
from .models import Words
from datetime import time
from django.utils import timezone

class EventForm(ModelForm):
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
			'English_word': forms.TextInput(attrs={'class':'form-control', 'placeholder':'איזו מילה תרצה להכניס למאגר?'}),
			'Hebrew_word': forms.TextInput(attrs={'class':'form-control', 'placeholder':'?מה הפירוש למילה'}),
			'How_To_Remember': forms.TextInput(attrs={'class':'form-control', 'placeholder':'מה האסוציאציה שחשבת עליה?'}),
			'Name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'מה השם שלך?'}),}
