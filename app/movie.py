import os
import json

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


class Movie:

    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title

    def get_movies(self):
        with open(DATA_FILE, 'r') as f:
            pass

    def write_movie(self):
        pass


if __name__ == "__main__":

    m = Movie("harry potter")
    print(m)
