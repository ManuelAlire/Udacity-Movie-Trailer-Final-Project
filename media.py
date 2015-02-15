import webbrowser #python standard library for displaying web based elements

#define Movie class
class Movie():
    #create space in memory for class and attributes title, storyline, boxoffice, poster_image_url, and trailer_youtube_url
    def __init__(self,movie_title, movie_storyline, box_office, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.boxoffice = box_office
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    #method opens web browser to display movie trailer    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
