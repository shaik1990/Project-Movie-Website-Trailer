import webbrowser

# Things for a class Movie to remember :
# title, storyLine, poster_image,ratings, reviews, show_trailer(), etc....

class Movie():

# when an instance of a movie is created, it invokes the __init__ constructor and initializes memory to that instance
# with the arguments passed every instance has its own unique attribute values.
# it is same as the this.x=x; in java.

    def __init__(self, title, poster, storyline, trailer ):

        self.title=title
        self.poster=poster
        self.storyline=storyline
        self.trailer=trailer

    def play_trailer(self):
        webbrowser.open(self.trailer)
        
        
