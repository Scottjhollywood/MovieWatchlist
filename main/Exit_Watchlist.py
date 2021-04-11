def exit_watchlist():
    choice = input("Are you happy with your watchlist experience?(Y/N): ")
    if choice.upper() == "Y":
        print("Thank you, have a nice day!")
    else:
        print("Apologies, we will attempt to make improvements")

    with open("C:/Users/Michael/PycharmProjects/MovieWatchlist/database/customer_response.txt", "a") as response:
        response.write(choice + "\n")
