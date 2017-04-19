from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
import json
import requests

# Create your views here.

def index(request):
    template = get_template('index.html')
    variables = Context({
        'Title' : 'Waifu FM App'
    })
    page = template.render(variables)
    return HttpResponse(page)

def inputdata(request): #sha de arreglar
	apikey = '0ef4f814ff3c3df0dc51fac9d7d234da'
	url_base = "http://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks&artist=cher&api_key="
	url_end = '&format=json'

	url = str(url_base) + str(apikey) + str(url_end)
	r = requests.get(url)
	json_data = json.loads(r.text)

	for track in json_data['toptracks']['track']:
	    name = track['name']
	    artist = track['artist']['name']

	    nameSong = form.cleaned_data[str(name)]
	    artistName = form.cleaned_data[str(artist)]

	    query1 = Artist(name=artistName, area='oda')
	    query2 = Song(name=nameSong,author=query1)
	    query1.save()
	    query2.save()
