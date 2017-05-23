from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from django.views.generic.edit import CreateView
from django.utils import timezone
from forms import ArtistForm, AlbumForm, AlbumReviewForm
from models import AlbumReview, Artist, Album


class HomepageView(TemplateView):
    template_name = 'index.html'


class AlbumListView(ListView):
    model = Album
    context_object_name = 'album_list'
    template_name = 'album_list.html'

'''
@login_required
class AlbumReviewCreate(CreateView):
    model = AlbumReview
    template_name = 'form.html'
    form_class = AlbumReviewForm
    success_url = reverse_lazy('waifufmapp:album_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.albumreview = AlbumReview.objects.get(id=self.kwargs['pk'])
        return super(AlbumReviewCreate, self).form_valid(form)
'''






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








'''
class ReviewDetail(DetailView):
	model = AlbumReview
	template_name = 'review_detail.html'

	def get_context_data(self, **kwargs):
		context = super(ReviewDetail, self).get_context_data(**kwargs)
		return context

class AlbumDetail(DetailView):
	model = Album
	template_name = 'album_detail.html'

	def get_context_data(self, **kwargs):
		context = super(AlbumDetail, self).get_context_data(**kwargs)
		return context

class AlbumCreate(CreateView):
    model = Album
    template_name = 'form.html'
    form_class = AlbumForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)


def review(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if AlbumReview.objects.filter(album=album, user=request.user).exists():
        AlbumReview.objects.get(album=album, user=request.user).delete()
    new_review = AlbumReview(
        rating=request.POST.get("rating", False),
        comment=request.POST.get("comment", False),
        user=request.user,
        date = timezone.now(),
        album= album
        )
    new_review.save()
    return HttpResponseRedirect("/")
'''