# coding = utf-8

"""
Module to display movie object, attributes and instances
"""
import webbrowser


class Movie():
    """
    Class object stores movie related information
    """

    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image, movie_trailer_youtube):
        """
        initialize instance of class Movie
        :param movie_title: title
        :param movie_storyline: storyline
        :param movie_poster_image: poster_image_url
        :param movie_trailer_youtube: trailer_youtube_url
        """

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_youtube

    def show_trailer(self):
        """
        initializing instance for opening the youtube video
        :return: webbrowser to play thriller
        """
        webbrowser.open(self.trailer_youtube)
