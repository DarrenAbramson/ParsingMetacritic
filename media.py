'''This file is largely unchanged from the Udacity provided template.

The key difference is the presence of self.metascore, which is obtained
by calling getmetascore.getscore.
'''

import webbrowser
import getmetascore

# getmetascore.getscore is called to retrieve the metascore.
# Notice that the normal, non-web-formatted version of the
# movie title is passed.


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_you
                 tube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.metascore = getmetascore.getscore(movie_title)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
