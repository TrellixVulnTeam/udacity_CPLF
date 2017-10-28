# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser


class Movie():
#define the Movie class

    def __init__(self, title, brief_story, poster_image_url, trailer_url, score):
        #init the movie info
        self.title = title
        self.brief_story = brief_story
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url
        self.score = score

    def show_trailer(self):
        #play the trailer
        webbrowser.open(self.trailer_url)