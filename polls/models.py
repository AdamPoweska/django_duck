# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    results_text = models.TextField(blank=True, null=True)
    duck_descriptions = models.TextField(blank=True, null=True) 
    favourite_ducks = models.TextField(blank=True, null=True) 
    duck_ratings = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.question_text

