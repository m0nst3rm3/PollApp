from django.db import models
import datetime
from django.utils import timezone
from django.contrib import admin


class Questions(models.Model):
    objects = ''
    question_text = models.CharField(max_length=400)
    published_on = models.DateTimeField("Published On:")

    @admin.display(
        boolean=True,
        ordering='published_on',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.published_on <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    DoesNotExist = ''
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

