from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Genre(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Artist(models.Model):
    name = models.TextField()
    area = models.TextField()
    biography = models.TextField(max_length = 20000, blank = True, null = True)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.TextField()
    date = models.DateField()
    author = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.name + " by " + str(self.author)

class Album(models.Model):
    name = models.TextField()
    #image = 
    area = models.TextField()
    year = models.IntegerField(max_length = 4)
    author = models.ForeignKey(Artist)
    Genre 

    def __unicode__(self):
        return self.name + " by " + str(self.author)


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    song = models.ForeignKey(Song)
    data = models.DateField()
    rating = models.PositiveSmallIntegerField("", blank = False, choices = RATING_CHOICES)

    def __unicode__(self):
        return self.song + ": " + str(self.rating)
