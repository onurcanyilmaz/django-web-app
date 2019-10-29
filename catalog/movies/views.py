from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Movie

# Create your views here.
def index(req):
    movies = Movie.objects.all()
    ctx = {
        'movies': movies
    }
    return render(req,'movies/list.html',ctx)
def detail(req,movie_id):
    movie = get_object_or_404(Movie,pk = movie_id)
    ctx = {
        'movie' : movie
    }
    return render(req,'movies/detail.html',ctx)
def search(req):
    return render(req,'movies/search.html')