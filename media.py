class Movie(object):
    """this class contains required attributes for Movie"""
    def __init__(self, title, poster_image_url, trailer_youtube_url, imdb_url, imdb_score, year):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.imdb_url = imdb_url
        self.imdb_score = imdb_score
        self.year = year
