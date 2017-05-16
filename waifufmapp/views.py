from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView

from forms import ArtistForm, AlbumForm
from models import AlbumReview, Artist, Album


# Create your views here.

def index(request):
    template = get_template('reviews_list.html')
    variables = Context({
        'Title' : 'Waifu FM App',
        'user': request.user
    })
    page = template.render(variables)

    return HttpResponse(page)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form
    return render_to_response('register.html', token)

@login_required
def log(request):
	#return HttpResponse("You have logged in successfuly")
	template = get_template('logged.html')
	variables = Context({
		'Title' : 'WaifuFM Login'
	})
	page = template.render(variables)
	return HttpResponse(page)

class ReviewDetail(DetailView):
	model = AlbumReview
	template_name = 'waifufmapp/review_detail.html'

	def get_context_data(self, **kwargs):
		context = super(ReviewDetail, self).get_context_data(**kwargs)
		return context

class ArtistDetail(DetailView):
	model = Artist
    #template = get_template('artist_detail.html')
	template_name = 'waifufmapp/artist_detail.html'

	def get_context_data(self, **kwargs):
		context = super(ArtistDetail, self).get_context_data(**kwargs)
		return context

def review(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if AlbumReview.objects.filter(album=album, user=request.user).exists():
        AlbumReview.objects.get(album=album, user=request.user).delete()
    new_review = AlbumsReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        album=album)
    new_review.save()
    return HttpResponseRedirect(reverse('waifufmapp:album_detail', args=(album.id,)))
