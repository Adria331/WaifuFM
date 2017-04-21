from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Genre(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Artist(models.Model):
    name = models.TextField(max_length = 20, null = False)
    area = models.TextField(max_length = 100)
    biography = models.TextField(max_length = 20000, blank = True, null = True)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.TextField(max_length = 20, null = False)
    date = models.DateField(default = date.today)
    author = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.name + ", by " + str(self.author)

class Album(models.Model):
    name = models.TextField(max_length = 20, null = False)
    image = models.ImageField(upload_to="picture_artist", blank=True, null=True)
    area = models.TextField(max_length = 100)
    year = models.IntegerField()
    author = models.ForeignKey(Artist)
    Genre = models.ForeignKey(Genre, default = None)

    def __unicode__(self):
        return self.name + ", by " + str(self.author)


class Review(models.Model):
    RATING_CHOICES = ((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))
    song = models.ForeignKey(Song)
    data = models.DateField()
    rating = models.PositiveSmallIntegerField("", blank = False, choices = RATING_CHOICES)

    def __unicode__(self):
        return self.song.name + ": " + str(self.rating)
