import media
import fresh_tomatoes

movies = [
    media.Movie("The Shawshank Redemption",
                "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                "http://www.youtube.com/watch?v=6hB3S9bIaco",
                '''
                Two imprisoned men bond over a number of years,
                    finding solace and eventual redemption through acts of common decency.''',
                1994),
    media.Movie("The Dark Knight",
                "http://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                "http://www.youtube.com/watch?v=yQ5U8suTUw0",
                '''
                When the menace known as the Joker wreaks havoc and chaos on the people of Gotham,
                the caped crusader must come to terms with one of the greatest psychological tests
                of his ability to fight injustice.''',
                2008),
    media.Movie("Pulp Fiction",
                "http://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                "http://www.youtube.com/watch?v=s7EdQ4FqbhY",
                '''
                The lives of two mob hit men, a boxer, a gangster's wife,
                and a pair of diner bandits intertwine in four tales of violence and redemption.''',
                1994),
    ]

fresh_tomatoes.open_movies_page(movies)
