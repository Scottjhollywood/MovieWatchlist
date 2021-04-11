from Movie_Extractor import FileExtractor
from Watchlist_Information import display_watchlist



def movie_selection():
    catalogue = FileExtractor.extract_movie_dict("movies_length.txt")
    watchlist = {}

    print("==================")
    print("Movie Catalogue")
    print("==================")
    for film in catalogue:
        print(film)
    print("==================")
    print("")
    decision = "Y"
    while decision.upper() == "Y":
        selection = input("Please select a film you would like to add to your watchlist: ")
        if selection in catalogue:
            watchlist[selection] = catalogue[selection]
            print(selection, "has been added to your watchlist!")
        else:
            print("Sorry we don't have that movie in our catalogue")

        decision = input("Would you like to add any other movie to your watchlist?(Y/N): ")

        if decision == "N":
            print(watchlist)
            display_watchlist(watchlist)



movie_selection()
