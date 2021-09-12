from django.db import models
from django.utils import timezone

# Create your models here.


class Analog(models.Model):
    First_word = models.CharField(max_length=30)
    Second_word = models.CharField(max_length=30)
    Third_word = models.CharField(max_length=30)
    Fourth_word = models.CharField(max_length=30)
    Sentence = models.TextField(max_length=150, blank=False)
    Difficulty = models.CharField(max_length=5)
    pub_date = models.DateTimeField(timezone.now(), null=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.First_word + " " + self.Second_word +" " + self.Third_word +" " + self.Fourth_word +" " + self.Sentence

class hebrew_words(models.Model):
    word = models.CharField(max_length=40 )
    meaning = models.CharField(max_length=40)
    Sentence = models.TextField(max_length=60, blank=False)
    pub_date = models.DateTimeField(timezone.now(), null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.word + " " + self.meaning + " " + self.Sentence

