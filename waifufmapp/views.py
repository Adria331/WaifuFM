from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from forms import ArtistForm, AlbumForm, AlbumReviewForm
from models import AlbumReview, Artist, Album
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator

#################################################################### Seguretat
class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'form.html'


##################################################################### Pagina Principal
class HomepageView(TemplateView): # ok
    template_name = 'index.html'


##################################################################### Llistes 
class AlbumListView(ListView): # ok
    model = Album
    context_object_name = 'album_list'
    template_name = 'album_list.html'


class ReviewListView(ListView): # ok
    model = AlbumReview
    context_object_name = 'review_list'
    template_name = 'reviews_list2.html'


##################################################################### Crear

class AlbumReviewCreate(LoginRequiredMixin, CreateView): # ok
    model = AlbumReview
    template_name = 'form.html'
    form_class = AlbumReviewForm
    success_url = reverse_lazy('waifufmapp:album_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumReviewCreate, self).form_valid(form)


#################################################################### Borrar

class ReviewDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = AlbumReview
    template_name = 'delete_review.html'
    success_url = reverse_lazy('waifufmapp:review_list')



##################################################################### Details


class AlbumDetail(DetailView): # ok
    model = Album
    template_name = 'album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        return context


class AlbumReviewDetail(DetailView):
    model = Album
    template_name = 'album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context











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