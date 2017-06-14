from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from django.utils import timezone

class Genre(models.Model):
    name = models.TextField()

    def __unicode__(self):
        return self.name

class Artist(models.Model):
    name = models.TextField(max_length = 200, null = False)
    location = models.TextField(max_length = 100, null = True)
    biography = models.TextField(max_length = 20000, blank = True, null = True)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.TextField(max_length = 200, null = False)
    date = models.DateField(default = date.today)
    author = models.ForeignKey(Artist, null = False)

    def __unicode__(self):
        return self.name + ", by " + str(self.author)

class Album(models.Model):
    name = models.TextField(max_length = 200, null = False)
    image = models.ImageField(upload_to="picture_artist", blank=True, null=True)
    location = models.TextField(max_length = 100)
    year = models.IntegerField(null=True)
    author = models.ForeignKey(Artist, null = False)
    Genre = models.ForeignKey(Genre, default = None, null = True)

    def __unicode__(self):
        return self.name + ", by " + str(self.author)

class AlbumReview(models.Model):
    RATING_CHOICES = ((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))
    comment = models.TextField(blank=True, default= "")
    date = models.DateField(default = timezone.now())
    album = models.ForeignKey(Album, null = False)
    userlocation = models.TextField(max_length = 100, null = True)
    user = models.ForeignKey(User, default=1)
    rating = models.PositiveSmallIntegerField("", blank = False, choices = RATING_CHOICES)


    def __unicode__(self):
        return "Review of: '" + str(self.album.name) + "', by " + str(self.user)

    def get_absolute_url(self):
        return reverse('waifufmapp:review_list', kwargs={'pkr': self.album.pk, 'pk': self.pk})
