from django.forms import ModelForm
from models import Artist, Album, AlbumReview

class ArtistForm(ModelForm):
	class Meta:
		model = Artist
		exclude = ('user', 'date',)

class AlbumForm(ModelForm):
	class Meta:
		model = Album
		exclude = ('user', 'date',)

class AlbumReviewForm(ModelForm):
	class Meta:
		model = AlbumReview
		exclude = ('user', 'date', 'album')