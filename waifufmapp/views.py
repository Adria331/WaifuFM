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

from serializers import AlbumSerializer, AlbumReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly



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
    success_url = reverse_lazy('waifufmapp:review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.album = Album.objects.get(id=self.kwargs['pk'])
        return super(AlbumReviewCreate, self).form_valid(form)


#################################################################### Borrar

class ReviewDelete(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    model = AlbumReview
    template_name = 'delete_review.html'
    success_url = reverse_lazy('waifufmapp:review_list')




################################################################# Details


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
        return context


################################################################## Users

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

def nolink(request):
    return HttpResponseRedirect('/waifufm')


########################################################## APIREST


class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class APIAlbumList(generics.ListCreateAPIView):
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class APIAlbumReviewList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    model = AlbumReview
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer

class APIAlbumReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = AlbumReview
    queryset = AlbumReview.objects.all()
    serializer_class = AlbumReviewSerializer



#APIAlbums, APIAlbumDetail, APIAlbumReviewList, APIAlbumReviewDetail