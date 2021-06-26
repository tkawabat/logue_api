from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
class User(models.Model):
    createdAt = models.DateField()
    updatedAt = models.DateField()
    deleted = models.BooleanField(default=False)
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    twitter = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id) + ': ' + self.name + '@' + self.twitter

class Scenario(models.Model):
    createdAt = models.DateField()
    updatedAt = models.DateField()
    deleted = models.BooleanField(default=False)
    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    author = models.BigIntegerField()
    text = models.CharField(max_length=100000)

    def __str__(self):
        return str(self.id) + ': ' + self.title