from Movie_Extractor import FileExtractor


def edit_watchlist(choices):
    movie_list = FileExtractor.extract_movie_dict("movies_length.txt")
    print("==================")
    print("Watchlist Editor")
    print("==================")
    print("1. Add movie(s) to your watchlist")
    print("2. Remove movie(s) from your watchlist")
    print("3. Exit")
    print("==================")
    editor_choice = int(input("Enter a number to continue: "))

    if editor_choice == 1:
        edit_list = "Y"
        print("==================")
        for movie in movie_list:
            print(movie)
        print("==================")

        while edit_list != "N":
            addition_choice = input("What movie would you like to add to your watchlist?: ")
            if addition_choice in movie_list:
                if addition_choice in choices:
                    print("That film is already in your watch list")
                else:
                    print(addition_choice, "has been added to your watchlist")
                    choices[addition_choice] = movie_list[addition_choice]
            else:
                print("We don't have that film in our selection")
            edit_list = input("Would you like to add anything else to your watchlist(Y/N):")
        return choices

    if editor_choice == 2:
        edit_list = "Y"
        print("==================")
        for movie in choices:
            print(movie)
        print("==================")

        while edit_list != "N":
            subtraction_choice = input("What movie would you like to remove from your watchlist?: ")
            if subtraction_choice in choices:
                choices.pop(subtraction_choice)
                print(subtraction_choice, "has been removed from your watchlist")

            else:
                print("You don't have that film in your watchlist")
            edit_list = input("Would you like to remove anything else to your watchlist(Y/N):")
        return choices

    if editor_choice == 3:
        return choices


