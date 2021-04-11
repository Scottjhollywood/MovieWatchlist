from Interface import WatchlistInterface


class ExtractorStub(WatchlistInterface):
    def extract_movie_dict(self):
        result = {"Hot Fuzz": 121, "Cast Away": 144, "The Fellowship of the Ring": 228}
        return result
