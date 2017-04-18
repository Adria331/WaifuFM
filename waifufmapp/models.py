from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    area = models.TextField()
    biography = models.TextField(max_length = 20000, blank = True, null = True)

class Genre(models.Model):
    name = models.TextField()

class Song(models.Model):
    name = models.TextField()
    date = models.DateField()

class Album(models.Model):
    name = models.TextField()
    #image =
    area = models.TextField()
    year = models.IntegerField(max_length = 4)

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    data = models.DateField()
    rating = models.PositiveSmallIntegerField("", blank = False, choices = RATING_CHOICES)
