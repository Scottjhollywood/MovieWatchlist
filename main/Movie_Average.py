from Movie_Extractor import FileExtractor


def movie_average(choices):
    total_rating = 0.0
    score_list = []
    ratings = FileExtractor.extract_movie_dict("movies_ratings.txt")
    for score in choices:
        score_list.append(ratings[score])
    for score in score_list:
        total_rating += float(score)
    average = round(total_rating / len(score_list), 1)
    return average



