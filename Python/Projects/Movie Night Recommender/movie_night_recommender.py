import random


movies = {
    "Action": ["John Wick", "The Dark Knight", "Mad Max: Fury Road"],
    "Comedy": ["The Hangover", "Superbad", "3 Idiots"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix"],
    "Horror": ["The Conjuring", "Get Out", "A Quiet Place"]
}


def display_genres():
    print("\n========== MOVIE NIGHT RECOMMENDER ==========")
    print("\nAvailable genres:")

    genres = list(movies.keys())

    for index, genre in enumerate(genres, start=1):
        print(f"{index}. {genre}")

    return genres


def get_genre_choice(genres):
    while True:

        choice = input("\nEnter your choice: ").strip()

        if not choice.isdigit():
            print("❌ Please enter a number.")
            continue

        choice = int(choice)

        if choice < 1 or choice > len(genres):
            print(f"❌ Please choose a number between 1 and {len(genres)}.")
            continue

        return genres[choice - 1]


def display_movies(genre):
    recommended_movies = movies[genre]

    print(f"\n🎬 Recommended {genre} Movies")
    print("---------------------------------------------")

    for index, movie in enumerate(recommended_movies, start=1):
        print(f"{index}. {movie}")


def random_recommendation(genre):
    movie = random.choice(movies[genre])

    print("\n🎲 Tonight's Random Pick")
    print("---------------------------------------------")
    print(f"🎬 {movie}")


def main():

    print("🎬 Welcome to Movie Night Recommender!")

    while True:

        genres = display_genres()

        genre = get_genre_choice(genres)

        display_movies(genre)

        random_recommendation(genre)

        while True:

            again = input(
                "\nWould you like another recommendation? (yes/no): "
            ).strip().lower()

            if again in ["yes", "y"]:
                break

            elif again in ["no", "n"]:
                print("\n🍿 Thanks for using Movie Night Recommender!")
                return

            else:
                print("❌ Please enter yes or no.")


main()
