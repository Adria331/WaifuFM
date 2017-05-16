from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Genre(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Artist(models.Model):
    name = models.TextField(max_length = 200, null = False)
    location = models.TextField(max_length = 100)
    biography = models.TextField(max_length = 20000, blank = True, null = True)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.TextField(max_length = 200, null = False)
    date = models.DateField(default = date.today)
    author = models.ForeignKey(Artist)

    def __unicode__(self):
        return self.name + ", by " + str(self.author)

class Album(models.Model):
    name = models.TextField(max_length = 200, null = False)
    image = models.ImageField(upload_to="picture_artist", blank=True, null=True)
    location = models.TextField(max_length = 100)
    year = models.IntegerField()
    author = models.ForeignKey(Artist)
    Genre = models.ForeignKey(Genre, default = None)

    def __unicode__(self):
        return self.name + ", by " + str(self.author)


class Review(models.Model):
    RATING_CHOICES = ((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))
    comment = models.TextField(blank=True, null=True)
    date = models.DateField()
    user = models.ForeignKey(User, default=1)
    rating = models.PositiveSmallIntegerField("", blank = False, choices = RATING_CHOICES)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.song.name + ": " + str(self.rating)


class AlbumReview(Review):
    album = models.ForeignKey(Album)

    class Meta:
        unique_together = ("album", "user")
