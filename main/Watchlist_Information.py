from Movie_Extractor import FileExtractor
from Movie_Average import movie_average
from Calculate_Time import calculate_time_hours
from Watchlist_Editor import edit_watchlist
from Exit_Watchlist import exit_watchlist


def display_watchlist(choices):
    decision = ""
    while decision != "N":
        print("==================")
        print("Your Watchlist")
        print("==================")
        for films in choices:
            print(films)
        print("==================")
        print("")
        print("==================")
        print("Watchlist Information")
        print("==================")
        print("1. Show movie rating(s)")
        print("2. Edit watchlist")
        print("3. Show movie(s) length")
        print("4. Exit")
        print("==================")
        print("")

        info_choice = int(input("Please enter a number: "))

        if info_choice == 1:

            print("==================")
            print("Movie Ratings")
            print("==================")
            ratings = FileExtractor.extract_movie_dict("movies_ratings.txt")
            for score in choices:
                print(score, ratings[score])
            print("==================")
            print("Average Rating:", movie_average(choices))
            decision = input("Would you like anymore information about your watchlist?(Y/N): ")

        elif info_choice == 2:
            choices = edit_watchlist(choices)
            display_watchlist(choices)
            decision = input("Would you like anymore information about your watchlist?(Y/N): ")

        elif info_choice == 3:
            print("==================")
            print("Movie(s) Length")
            print("==================")
            movie_time_hours = calculate_time_hours(choices)
            for movie in movie_time_hours:
                print(movie, str(movie_time_hours[movie][0]) + "h", str(movie_time_hours[movie][1]) + "m")
            print("==================")
            total_time = {}
            total_time_minutes = 0
            for time in choices:
                total_time_minutes += int(choices[time])
            total_time["total"] = total_time_minutes
            total_time_hours = calculate_time_hours(total_time)
            print("Total time to watch:", str(total_time_hours["total"][0]) + "h", str(total_time_hours["total"][1]) + "m")
            decision = input("Would you like anymore information about your watchlist?(Y/N): ")

        elif info_choice == 4:
            decision = "N"
            exit_watchlist()

        else:
            print("Error not a valid choice")

        if info_choice != 4:
            if decision == "N":
                exit_watchlist()



