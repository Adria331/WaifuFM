from django.forms import ModelForm
from models import Artist, Album

class ArtistForm(ModelForm):
	class Meta:
		model = Artist
		exclude = ('user', 'date',)

class AlbumForm(ModelForm):
	class Meta:
		model = Album
		exclude = ('user', 'date', 'artist',)
