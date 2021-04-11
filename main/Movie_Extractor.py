from Interface import WatchlistInterface
import pathlib


class FileExtractor(WatchlistInterface):

    def extract_movie_dict(self):

        catalogue = {}
        with open("C:/Users/Michael/PycharmProjects/MovieWatchlist/database/" + self, "r") as file:
            for movies in file.readlines():
                movies = movies.strip()
                movies = movies.split("^")
                catalogue[movies[0]] = movies[1]

        return catalogue


