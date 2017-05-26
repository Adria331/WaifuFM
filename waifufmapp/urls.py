from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from models import Album, Artist, AlbumReview
from forms import ArtistForm, AlbumForm, AlbumReviewForm
from views import HomepageView, AlbumListView, AlbumReviewCreate, ReviewListView, ReviewDelete, LoginRequiredCheckIsOwnerUpdateView, AlbumDetail, AlbumReviewDetail, APIAlbumList, APIAlbumDetail, APIAlbumReviewList, APIAlbumReviewDetail
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', HomepageView.as_view()),

    #Llistes
    url(r'^albums/$', AlbumListView.as_view(), name = 'album_list',),
    url(r'^reviews/$', ReviewListView.as_view(), name = 'review_list',),

    #Tractament de reviews
    url(r'^albums/(?P<pk>\d+)/reviews/create/$', AlbumReviewCreate.as_view(), name = 'review_create',),
    url(r'^albums/(?P<pkr>\d+)/reviews/(?P<pk>\d+)/delete/$', ReviewDelete.as_view(), name='review_delete'),
    url(r'^albums/(?P<pkr>\d+)/reviews/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=AlbumReview,
           template_name='form.html',
           success_url='/waifufm/reviews',
            form_class=AlbumReviewForm),
        name='review_edit'),

    #Detalls
    url(r'^albums/(?P<pk>\d+)/$', AlbumDetail.as_view(), name='album_detail'),
    url(r'^albums/(?P<pkr>\d+)/reviews/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=AlbumReview,
            template_name='reviews_detail.html'),
        name='review_detail'),
]



urlpatterns += [
    # RESTful API
    url(r'^api/albums/$',
        APIAlbumList.as_view(), name='album-list'),
    url(r'^api/albums/(?P<pk>\d+)/$',
        APIAlbumDetail.as_view(), name='album-detail'),
    url(r'^api/albumreviews/$',
        APIAlbumReviewList.as_view(), name='albumreview-list'),
    url(r'^api/albumreviews/(?P<pk>\d+)/$',
        APIAlbumReviewDetail.as_view(), name='albumreview-detail'),
]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])


