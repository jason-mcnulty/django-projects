import requests
from django.shortcuts import render

# Create your views here.
def index(request):

    #url = 'http://www.omdbapi.com/?t=back+to+the+future&apikey=676ef45a'

    url = 'http://www.omdbapi.com/?t={}&apikey=676ef45a'
    movie = 'braveheart'

    r = requests.get(url.format(movie)).json()
    #print(r.text)


    #movie_info = {'insert_me': "Hello I am looking at this"}
    movie_info = {

    'Title' : r['Title'],
    'Year' :  r['Year'],
    'Actors' : r['Actors'],
    'Poster' : r['Poster'],

    }

    #context = {'city_weather' : movie_info}
    return render(request, 'weather/index.html', context=movie_info)
