import os
import json
import logging
import sys


CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json").replace("\\", "/")


def get_movies():
    with open(DATA_FILE, 'r') as f:
        movies_titles = json.load(f)

    return [Film(movie_title) for movie_title in movies_titles]


class Film:

    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_FILE, 'w') as f:
            json.dump(movies, f, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()

        if self.title not in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"film déjà enregistré {self.title}")
            return False

    def delete_from_movies(self):
        movies = self._get_movies()

        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
