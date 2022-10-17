import sqlite3
from request import *


def search_film_for_title(title_name):

    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(request_1(title_name))
        for content in cursor.fetchall():
            film = {'title': content[0],
                    'country': content[1],
                    'release_year': content[2],
                    'genre': content[3],
                    'description': content[4]}
        return film


def group_film_for_release_years(year_1, year_2):
    films = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(request_2(year_1, year_2))
        for content in cursor.fetchall():
            film = {'title': content[0],
                    'release_year': content[1]}
            films.append(film)
        return films


def search_film_for_rating(rating_name):
    films = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(request_3(rating_name))
        for content in cursor.fetchall():
            film = {'title': content[0],
                    'rating': content[1],
                    'description': content[2]}
            films.append(film)
        return films


def search_film_for_genre(genre):
    films = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(request_4(genre))
        for content in cursor.fetchall():
            genre_list = content[2].split(', ')
            if genre in genre_list:
                film = {'title': content[0],
                        'description': content[1]}
                films.append(film)
        return films


def actors_playing_together_3_or_more_times(name_1, name_2):
    casts = []
    actors = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(request_5(name_1, name_2))
        for content in cursor.fetchall():
            casts.extend(content[1].split(', '))
            for actor in set(casts):
                if casts.count(actor) > 2:
                    actors.append(actor)
    actors.remove(name_1)
    actors.remove(name_2)
    return actors


def search_film_from_type_name_genre_year(type_name, genre, year):
    films = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        cursor.execute(request_6(type_name, genre, year))
        for content in cursor.fetchall():
            genre_list = content[2].split(', ')
            if genre in genre_list:
                film = {'title': content[0],
                        'description': content[1]}
                films.append(film)
        return films
