from app import app
from flask import render_template,request
from .requests import get_movies, get_movie_id


@app.route('/', methods=['GET'])
def index():
    movie_selction = request.form.get('movies_option')
    data_link = get_movies('popular')
    return render_template('index.html', data_link= data_link)

@app.route("/upcoming")
def upcoming():
    data_link = get_movies('upcoming')
    return render_template('upcoming.html', data_link= data_link)

@app.route("/now_playing")
def now_playing():
    data_link = get_movies('now_playing')
    return render_template('now_playing.html', data_link= data_link)

@app.route('/movie/<int:movie_id>')
def movie_id(movie_id):
    movie = get_movie_id(movie_id)
    title = f"{movie.title}"
    return render_template('movie.html', title=title ,movie= movie_id)
