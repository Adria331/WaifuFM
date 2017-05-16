from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from models import Album, Artist, AlbumReview
from forms import ArtistForm, AlbumForm
from views import ArtistDetail, ReviewDetail

urlpatterns = [
# List latest 10 artists: /artists/
    url(r'\^\$',
        ListView.as_view(
            queryset=AlbumReview.objects.filter(date__lte=timezone.now()).order_by('-date')[:2],
            context_object_name='latest_reviews_list',
            template_name='review/reviews_list.html'),
        name='reviews_list'),
# Artists details, ex.: /waifufm/artists/1/
    url(r'\^artists/(?P<pk>\d+)/\$',
        ArtistDetail.as_view(),
        name='artists_detail'),
# Album details, ex:  /waifufm/artists/1/albums/1/
    url(r'\^artists/(?P<pkr>\d+)/albums/(?P<pk>\d+)/\$',
        DetailView.as_view(
        	model=Album,
        	template_name='artists/album_detail.html'),
        name='album_detail'),
# Create a album review, ex.: /waifufm/artists/1/albums/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    url(r'\^artists/(?P<pk>\\d+)/reviews/create/\$',
    	'waifufm.views.review',
    	name='review_create'),
]
