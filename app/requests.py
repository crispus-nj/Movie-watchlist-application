from app import app
import requests
import urllib, json
from .models import movies

Movie = movies.Movie

API_KEY = app.config['MOVIE_API_KEY']
base_url = app.config['MOVIE_API_BASE_URL']

def get_movies(category):
    base_url_data = base_url.format(category, API_KEY)
    movies_data = requests.get(base_url_data).json()
    movie_data = []
    for data in movies_data['results']:
        id = data['id']
        title = data['title']
        overview = data['overview']
        poster = data['poster_path']
        vote_average= data['vote_average']
        vote_count = data['vote_count']
        movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
        movie_data.append(movie_object)
    print(type(movie_data))
    return movie_data

def get_movie_id(id):
    # base_url_data = base_url.format(id, API_KEY)
    # movie_data = requests.get(base_url_data)

    # movie_data_id = None
    # if movie_data:
    #     ids = movie_data['results'].id
    #     title = movie_data['results'].title
    #     overview = movie_data['results'].overview
    #     poster = movie_data['results'].poster_path
    #     vote_average = movie_data['results'].vote_average
    #     vote_count = movie_data['results'].vote_count
    #     movie_object = Movie(ids, title, overview, poster, vote_average, vote_count)
    #     movie_data_id = movie_object

    # for data in movie_data['results']:
    #     ids = data['id']
    #     title = data['title']
    #     overview = data['overview']
    #     poster = data['poster_path']
    #     vote_average= data['vote_average']
    #     vote_count = data['vote_count']
    #     movie_object = Movie(ids, title, overview, poster, vote_average, vote_count)
    #     movie_data_id = movie_object

    get_movie_details_url = base_url.format(id,API_KEY)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id = movie_details_response.get('id')
            title = movie_details_response.get('original_title')
            overview = movie_details_response.get('overview')
            poster = movie_details_response.get('poster_path')
            vote_average = movie_details_response.get('vote_average')
            vote_count = movie_details_response.get('vote_count')

            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

    return movie_object
