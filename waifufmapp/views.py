from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    template = get_template('index.html')
    variables = Context({
        'Title' : 'Waifu FM App'
    })
    page = template.render(variables)
    return HttpResponse(page)
