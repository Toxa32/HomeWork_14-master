from utils import *
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def film_for_title(title):
    film = search_film_for_title(title)
    return jsonify(film)


@app.route('/movie/<year_1>/to/<year_2>')
def film_for_year(year_1, year_2):
    films = group_film_for_release_years(year_1, year_2)
    return films


@app.route('/rating/children')
def film_for_children():
    rating_name = ['G']
    films = search_film_for_rating(rating_name)
    return films


@app.route('/rating/family')
def film_for_family():
    rating_name = ['G', 'PG', 'PG-13']
    films = search_film_for_rating(rating_name)
    return films


@app.route('/rating/adult')
def film_for_adult():
    rating_name = ['R', 'NC-17']
    films = search_film_for_rating(rating_name)
    return films


@app.route('/genre/<genre>')
def film_for_genre(genre):
    films = search_film_for_genre(genre)
    return films


if __name__ == "__main__":
    app.run()
