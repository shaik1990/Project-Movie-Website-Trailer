Project-Movie-Website-Trailer
-----------------------------

-------To create a web Page using Python-----
  Install python.
A new file show.py with class Movie() is created with a constructor __init__ with instance variables or attributes such as poster_image, youtube_url, title, storyline, ratings, review etc..
An instance of every movie is created in another file zoom.py where show.Movie class is invoked with unique object and the parameter values are passed
__init__ constructor, when ever an instance of the class movie is created, all the variables are initialized their values accordingly to the arguments passed.
Create instance methods/functions like show trailer, read review, comment review etc..
In zoom.py, instances are created with respect to	the class movie(). For example, to every movie that should be	listed on the web page(fresh_tomatoes.py) an instance is created and arguments are passed so that the values are 	initialized. All the instances created are added to a list (movies) and movies list is passed as argument into the method (open_movies_page).
fresh_tomatoes.py-- A html file, with css and script tags to perfectly manage the outlook of the page.
For every instance(Movie object) created are displayed in the webpage by fresh_tomatoes.py file with invoking open_movies_page(movies list)
