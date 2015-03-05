import webbrowser

class Movie():
    """
    Movie creates an instance object with relevant information passed in to define a movie.

    instance variables:
        title
        storyline
        boxoffice
        poster_image_url
        trailer_youtube_url
    public procedures:
        show_trailer()
    """
    def __init__(self,movie_title, movie_storyline, box_office, poster_image, trailer_youtube):
        """
        Movie Class constructor, creates space in memory and assigns arguments to accessible varibles.
        
        arguments:
            movie_storyline - string describing storyline of movie
            box_office - int of of global box office receipts
            poster_image - url of box office movie poster
            trailer_youtube - url of youtube movie trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.boxoffice = box_office
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    
    def show_trailer(self):
        """
        show_trailer procedure opens browser and shows youtube trailer of Movie instance.
        """
        webbrowser.open(self.trailer_youtube_url)
