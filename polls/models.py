from django.db import models
from django.utils import timezone

# Create your models here.


class Words(models.Model):
    English_word = models.CharField(max_length=30, unique=True)
    Hebrew_word = models.CharField(max_length=30)
    How_To_Remember = models.TextField(max_length=60, blank=False)
    Name = models.CharField(max_length=20, null=True)
    pub_date = models.DateTimeField(timezone.now(), null=True)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return self.English_word +" " + self.Hebrew_word +" " + self.How_To_Remember +" " + self.Name


