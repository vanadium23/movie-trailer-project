class Movie(object):
    """this class contains required attributes for Movie"""
    def __init__(self, title, poster_image_url, trailer_youtube_url, description, year):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.description = description
        self.year = year
