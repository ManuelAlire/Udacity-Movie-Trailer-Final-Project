import media
import fresh_tomatoes

interstellar = media.Movie("Intersellar",
                           "Mathew McConaughey goes into deep space for reasons, alright, alright, alright....",
                           "671,659,681",	
                           "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

mean_girls = media.Movie("Mean Girls",
                         "Home schooled girl goes to public high school for the first time and stuggles to adjust.",
                         "129,042,871",
                         "http://upload.wikimedia.org/wikipedia/en/8/8f/Mean_Girls_movie.jpg",
                         "https://www.youtube.com/watch?v=KAOmTMCtGkI")

full_metal_jacket = media.Movie("Full Metal Jacket",
                                "R. Lee Ermey trains a bunch of whiney baby boomers to fight the vietnam war, they lose. Oh, its about mind control.",
                                "46357676",
                                "http://upload.wikimedia.org/wikipedia/en/9/99/Full_Metal_Jacket_poster.jpg",
                                "https://www.youtube.com/watch?v=x9f6JaaX7Wg")

blue_is_the_warmest_color = media.Movie("Blue Is The Warmest Color",
                                        "Girl meets Girl, they fall in love, they grow up, and grow apart.",
                                        "7,379,806",	
                                        "http://upload.wikimedia.org/wikipedia/en/9/9e/La_Vie_d%27Ad%C3%A8le_%28movie_poster%29.jpg",
                                        "https://www.youtube.com/watch?v=uKmWi_T3QWE")

her = media.Movie("Her",
                  "Man falls in love with his A.I. computer, which is totally not the same situation im in. I spend a lot of time with my computer, but we are not in love.",
                  "$47,351,251",	
                  "http://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg",
                  "https://www.youtube.com/watch?v=WzV6mXIOVl4")

when_we_were_kings = media.Movie("When We Were Kings",
                  "Documentary about Muhammed Ali's greatest fight 'The Rumble In The Jungle' ",
                  "$2,789,985",
                  "http://upload.wikimedia.org/wikipedia/en/0/0d/When_We_Were_Kings_DVD_Cover_art.jpg",
                  "https://www.youtube.com/watch?v=IfUHYUpmTFs")

the_sunset_limited = media.Movie("The Sunset Limited",
                                 "Suicidal atheist is rescued by a theist while attempting to jump in front of a train. They have a philosophical discussion about god, life, and the nature of reality.",
                                 "$0",
                                 "http://upload.wikimedia.org/wikipedia/en/3/3a/The_Sunset_Limited.jpg",
                                 "https://www.youtube.com/watch?v=l0MSitTAYyA")

the_usual_suspects = media.Movie("The Usual Suspects",
                                 "International crime boss hides in plain sight, and is one step ahead of everyone. which is not a surpise since keyser sozey is kevin spacey.",
                                 "$23,341,568",
                                 "http://upload.wikimedia.org/wikipedia/en/9/9c/Usual_suspects_ver1.jpg",
                                 "https://www.youtube.com/watch?v=oiXdPolca5w")

predator = media.Movie("Predator",
                       "Alien comes to earth to hunt humans, but picks the wrong prey.",
                       "$98,267,558",
                       "http://upload.wikimedia.org/wikipedia/en/9/95/Predator_Movie.jpg",
                       "https://www.youtube.com/watch?v=Y1txEAywdiw")


movies = [interstellar, the_sunset_limited, full_metal_jacket, her, when_we_were_kings, predator, the_usual_suspects, blue_is_the_warmest_color, mean_girls]
fresh_tomatoes.open_movies_page(movies)
