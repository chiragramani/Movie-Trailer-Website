# Importing module webbrowser since for show_trailer procedure, we need to open the url
import webbrowser

# Class - Movie
class Movie():
    # Constructor - initiliazing the instance of class Movie with necessary instance properties
    def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube):
        # The title of the movie
        self.title = movie_title

        # The storyline of the movie
        self.storyline = movie_storyline

        # The link containing the poster_image
        self.poster_image_url = movie_poster_image

        # The youtube link of the movie's trailer
        self.trailer_youtube_url = movie_trailer_youtube

    # Opens the trailer in the default web-browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube)
