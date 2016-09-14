import show, fresh_tomatoes, urllib

# instances are created for each movie
# pass the arguments to be displayed to the __init__ constructor

dexter=show.Movie("Dexter",
                   "http://i00.i.aliimg.com/wsphoto/v0/2029152520/P0104-24x32-font-b-Dexter-b-font-font-b-6-b-font-TV-font-b-series.jpg",
                   "A forensics expert finding out the bad guys, stalking and killing them to overcome his urges",
                   "https://www.youtube.com/watch?v=YQeUmSD1c3g")
mechanic=show.Movie("Mechanic: Resurrection",
                     "http://loadtv.biz/wp-content/uploads/2016/08/mechanic-resurrection.jpg",
                     "",
                     "https://www.youtube.com/watch?v=QF903RaKLvs")
 
squad=show.Movie("Suicide Squad",
                  "http://www.darkknightnews.com/wp-content/uploads/2016/06/Suicide-Squad.jpg",
                  "",
                  "https://www.youtube.com/watch?v=CmRih_VtVAs")
breathe=show.Movie("Don`t Breathe",
                    "http://www.blogbusters.ch/wp-content/uploads/2016/05/dont-breathe-blogbusters-filmdatenbank.jpg",
                    "",
                    "https://www.youtube.com/watch?v=S8XwWwPT8LE")
bourne=show.Movie("Jason Bourne",
                   "http://www.hollywoodjesus.com/movie/bourne_identity/bourne_identity.jpg",
                   "",
                   "https://www.youtube.com/watch?v=F4gJsKZvqE4")
deadpool=show.Movie("Deadpool",
                     "http://www.flickeringmyth.com/wp-content/uploads/2016/01/Deadpool-poster-2.jpg",
                     "",
                     "https://www.youtube.com/watch?v=Xithigfg7dA")
batman=show.Movie("Batman Begins",
                   "http://i2.listal.com/image/134556/600full-batman-begins-poster.jpg",
                   "",
                   "https://www.youtube.com/watch?v=neY2xVmOfUM")
jungle=show.Movie("The Jungle Book",
                   "http://images.mid-day.com/images/2016/mar/24The-Jungle-Book-1.jpg",
                  "",
                   "https://www.youtube.com/watch?v=5mkm22yO-bs")
warrior=show.Movie("Warrior",
                    "http://1.bp.blogspot.com/-9HFHnlxd8Wk/UQGfJVMZjRI/AAAAAAAAAFk/cCElVmqdaaU/s1600/warrior-film-poster-large.jpg",
                    "",
                    "https://www.youtube.com/watch?v=_jmY_khwLs8")
bridge=show.Movie("Bridge of Spies",
                   "http://www.blackfilm.com/read/wp-content/uploads/2015/06/Bridge-of-Spies-poster.jpg",
                   "",
                   "https://www.youtube.com/watch?v=jxUk1RsajcI")
panda=show.Movie("Kung fu Panda",
                  "http://oneguyrambling.com/wp-content/uploads/2011/06/kung_fu_panda.jpg",
                  "",
                  "https://www.youtube.com/watch?v=GYIkexIdd-8")
prison=show.Movie("Prison Break| season 5",
                   "http://3.bp.blogspot.com/-gyUym5v_UEk/UBcGwd4ZAMI/AAAAAAAAAPw/g25C0UoIa7k/s1600/prison-break_0001.jpg",
                   "",
                   "https://www.youtube.com/watch?v=x9T-9fZn_oA")
breaking=show.Movie("Breaking bad",
                     "http://pics.filmaffinity.com/Breaking_Bad_TV_Series-398069237-large.jpg",
                     "",
                     "https://www.youtube.com/watch?v=HhesaQXLuRY")

 # A List is created to add all the movies to be shown on the web page(fresh_tomatoes)
# if the movie is not added to the list then the movie is not at all shown on the webpage.

movies=[dexter,mechanic, squad, breathe, bourne, deadpool,batman, jungle, warrior, bridge, panda, prison, breaking]
fresh_tomatoes.open_movies_page(movies)
 
    





