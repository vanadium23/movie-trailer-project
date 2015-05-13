import media
import fresh_tomatoes

movies = [
    media.Movie("The Shawshank Redemption",
                "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                "http://www.youtube.com/watch?v=6hB3S9bIaco",
                "http://www.imdb.com/title/tt0111161/",
                9.3,
                1994),
    media.Movie("The Dark Knight",
                "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                "http://www.youtube.com/watch?v=yQ5U8suTUw0",
                "http://www.imdb.com/title/tt0468569/",
                9.0,
                2008),
    media.Movie("Pulp Fiction",
                "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                "http://www.youtube.com/watch?v=s7EdQ4FqbhY",
                "http://www.imdb.com/title/tt0110912/",
                8.9,
                1994),
    media.Movie("Inception",
                "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                "http://www.youtube.com/watch?v=66TuSJo4dZM",
                "http://www.imdb.com/title/tt1375666/",
                8.8,
                2010),
    media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                "http://www.youtube.com/watch?v=JNwNXF9Y6kY",
                "http://www.imdb.com/title/tt0080684/",
                8.8,
                1980),
    ]

fresh_tomatoes.open_movies_page(movies)
