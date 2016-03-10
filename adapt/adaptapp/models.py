from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class User(models.Model):
#    name = models.CharField(max_length=200)
#    password = models.CharField(max_length=16)

class Question(models.Model):
    question = models.CharField(max_length=50) # a URL

class UserRecord(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    whenans = models.DateTimeField('last time answered')
    correct = models.BooleanField('answer was correct?')
    nexttime = models.DateTimeField('the next time we show this question to this user')

