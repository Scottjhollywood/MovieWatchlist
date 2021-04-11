def calculate_time_hours(time):
    movie_length_hours = time.copy()

    for length in movie_length_hours:
        movie_length_hours[length] = 0

    for hours in time:
        movie_length_hours[hours] = [int(time[hours]) // 60, int(time[hours]) % 60]

    return movie_length_hours




