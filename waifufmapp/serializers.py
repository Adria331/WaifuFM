from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Album, AlbumReview


class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='waifufmapp:album-detail')
    albumreview_set = HyperlinkedRelatedField(many=True, read_only=True,
                                                   view_name='waifufmapp:albumreview-detail')
    

    class Meta:
        model = Album
        fields = ('uri', 'name', 'year', 'albumreview_set')


class AlbumReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='waifufmapp:albumreview-detail')
    album = HyperlinkedRelatedField(view_name='waifufmapp:album-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = AlbumReview
        fields = ('uri', 'rating', 'comment', 'user', 'date', 'userlocation', 'album')