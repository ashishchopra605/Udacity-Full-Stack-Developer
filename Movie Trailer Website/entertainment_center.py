import media
import fresh_tomatoes

"""
declare favorite movies, with 4 arguements each:
title (movie's title)
storyline (movie's storyline)
poster_url (url to poster image)
trailer_url (url to youtube trailer)
"""

toystory = media.Movie("Toy Story",
                       "A story of a boy and his toys that come to life",
                       "http://www.gstatic.com/tv/thumb/movieposters/"
                       "17420/p17420_p_v8_ab.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=1s")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://static.rogerebert.com/uploads/movie/"
                             "movie_poster/school-of-rock-2003/"
                             "large_cREN222Yw78zvSQ9bg17Y9QZS0c.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

avatar = media.Movie("Avatar",
                     "A marine on an alien Planet",
                     "http://t0.gstatic.com/images?q=tbn:A"
                     "Nd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

hunger_games = media.Movie("Hunger Games",
                           "A really rael reality show",
                           "http://t2.gstatic.com/images?q=tbn:A"
                           "Nd9GcS58mYVyiI3LTihImFjn6QBL"
                           "U_mcHXZP3LaGoWN9u5bzuvW3lvC",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "going back in time to meet authors",
                                "http://t3.gstatic.com/images?q=tbn:A"
                                "Nd9GcTk3ssys2bKM5-U6XMgv"
                                "oD8yVoS5Io2YKg_1xA6x6GA8mKuuqID",
                                "https://www.youtube.com/watch?v=dtiklALGz20")

fast_furious = media.Movie("Furious 7",
                           "Dominic and his family are caught in a qu"
                           "agmire when Shaw's brother seeks bloody revenge.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcReedjA2vJ"
                           "SO4_6GDpsI3PShvbRqfAAEv03qaJ9qOxtiLZX0Jx7",
                           "https://www.youtube.com/watch?v=yISKeT6sDOg")

# assign movies to movies array
movies = [toystory, school_of_rock, avatar,
          hunger_games, midnight_in_paris, fast_furious]
fresh_tomatoes.open_movies_page(movies)
