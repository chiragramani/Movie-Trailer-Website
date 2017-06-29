# Importing media, this has the definitions for class Movie
import media
# Importing fresh_tomatoes, since this will take a list of movies, format them, makes an html page out of it and open the same in a web-browser.
import fresh_tomatoes

# Movie - The Dark Knight Rises, an instance of class Movie.
the_dark_knight_rises = media.Movie("The Dark Knight Rises", "Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace. This forces Bruce Wayne to come out of hiding and don the cape and cowl of Batman again.",
                                    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                                    "https://www.youtube.com/watch?v=g8evyE9TuYk")

# Movie - Avatar, an instance of class Movie.
avatar = media.Movie("Avatar", "Jake, a paraplegic marine, replaces his brother on the Na'vi inhabited Pandora for a corporate mission. He is accepted by the natives as one of their own but he must decide where his loyalties lie.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# Movie - Inception, an instance of class Movie.
inception = media.Movie("Inception", "Cobb steals information from his targets by entering their dreams. He is wanted for his alleged role in his wife's murder and his only chance at redemption is to perform the impossible, an inception.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

# Movie - The Pursiot Of Happiness, an instance of class Movie.
the_pursuit_of_happiness = media.Movie("The Pursuit of Happyness", "Chris Gardner takes up an unpaid internship in a brokerage firm after he loses his life's earnings selling a product he invested in. His wife leaves him and he is left with the custody of his son.",
                                    "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",
                                    "https://www.youtube.com/watch?v=bTJ-0zVAsEA")

# Movie - Bhaag Milkha Bhaag, an instance of class Movie.
bhaag_milkha_bhaag = media.Movie("Bhaag Milkha Bhaag", "Milkha Singh or the 'Flying Sikh' overcomes many agonising obstacles to become a world champion, Olympian and one of India's most iconic athletes.",
                                "https://upload.wikimedia.org/wikipedia/en/4/42/Bhaag_Milkha_Bhaag_poster.jpg",
                                "https://www.youtube.com/watch?v=u71swQ4ksgI")

# Movie - Dangal, an instance of class Movie.
dangal = media.Movie("Dangal", "After his failure at winning a gold medal for the country, Mahavir Phogat, despite societal pressures, vows to realize his dreams by training his daughters for the Commonwealth Games.",
                    "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                    "https://www.youtube.com/watch?v=x_7YlGv9u1g")

# A list of my favorite movies
my_favorite_movies = [the_dark_knight_rises, avatar, inception, the_pursuit_of_happiness, bhaag_milkha_bhaag, dangal]

# Procedure which accepts a list of movies, formats them, makes an html page out of it and open the same in a web-browser
fresh_tomatoes.open_movies_page(my_favorite_movies)
