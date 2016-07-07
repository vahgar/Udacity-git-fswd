import webbrowser

#defining class for movies so that different instaces can be made
class Movie():
    #Constructor for movie object
    def __init__(self,movie_title,movie_storyline,movie_poster,movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    #fuction to show trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
