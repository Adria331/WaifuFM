from django.contrib.auth.models import User
from django.test import TestCase
from models import Album, AlbumReview, Artist

class AlbumReviewTestCase(TestCase):

	user1 = None
	user2 = None


	def setUp(self):
		#Artist.objects.create(name="Flako")

		StarWars = Album.objects.create(name="StarWars", author=Artist.objects.create(name="Flako"))

		user1 = User.objects.create(username="user1")
		user2 = User.objects.create(username="user2")

		AlbumReview.objects.create(rating=1, comment="Trash!", album=StarWars, user=user1)
		AlbumReview.objects.create(rating=5, comment="Coponudisimo!!", album=StarWars, user=user2)


	def test_checkAuthor(self):
		albumr = AlbumReview.objects.get(id=1)
		self.assertEqual(str(albumr.album.author), 'Flako')
