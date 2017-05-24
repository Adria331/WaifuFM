from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Album, Artist, AlbumReview
from forms import ArtistForm, AlbumForm, AlbumReviewForm
from views import HomepageView, AlbumListView, AlbumReviewCreate, ReviewListView, ReviewDelete, LoginRequiredCheckIsOwnerUpdateView
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^$', HomepageView.as_view()),
    url(r'^albumlist/$', AlbumListView.as_view(), name = 'album_list',), #List of albums
    url(r'^reviewlist/$', ReviewListView.as_view(), name = 'review_list',),

    url(r'^review/create/$', AlbumReviewCreate.as_view(), name = 'review_create',),
    url(r'^review/(?P<pk>\d+)/delete/$', ReviewDelete.as_view(), name='review_delete'),
    url(r'^review/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=AlbumReview,
            template_name='form.html',
            form_class=AlbumReviewForm),
        name='review_edit'),

]




'''

    url(r'\^albums/(?P<pk>\d+)/\$',
        AlbumDetail.as_view(),
        name='album_detail'),

    url(r'\^album/(?P<pkr>\d+)/details/(?P<pk>\d+)/\$',
        DetailView.as_view(
            model=Album,
            template_name='album_detail.html'),
        name='album_detail'),

    url(r'\^album/(?P<pkr>\d+)/review/(?P<pk>\d+)/\$',
        DetailView.as_view(
            model=Album,
            template_name='album_review.html'),
        name='album_review'),

# Create a album review, ex.: /waifufm/artists/1/albums/1/reviews/create/
# Unlike the previous patterns, this one is implemented using a method view instead of a class view
    url(r'\^album/(?P<pk>\\d+)/reviews/create/\$',
        'waifufmapp.views.review',
        name='review_create'),
'''