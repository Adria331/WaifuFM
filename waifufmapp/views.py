from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    template = get_template('index.html')
    variables = Context({
        'Title' : 'Waifu FM App',
        'user': request.user
    })
    page = template.render(variables)

    return HttpResponse(page)

@login_required
def homepage(request):
	return HttpResponse("Temporal Homepage")

def register(request):
    template = get_template('register.html')
    variables = Context({
        'Title' : 'Registration',
    })
    page = template.render(variables)

@login_required
def log(request):
	#return HttpResponse("You have logged in successfuly")
	template = get_template('logged.html')
	variables = Context({
		'Title' : 'WaifuFM Login'
	})
	page = template.render(variables)
	return HttpResponse(page)