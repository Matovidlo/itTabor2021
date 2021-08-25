import requests

from django.shortcuts import render


def index(request):
    # TODO: this is old api call
    #movies = requests.get("http://localhost:5000/Mato/movies")    
    movies = requests.get("http://localhost:5000/beautiful-movies")
    movies = movies.json()
    return render(request, 'index.html', {'title': 'movies', 'movies': movies})
# Create your views here.
def time(request):
    response = requests.get("http://localhost:5000/time")
    current_time = response.content.decode("utf-8")
    return render(request, 'time.html', {'time': current_time})
