from media import Movie
import fresh_tomatoes


toy_story = Movie("Toy Story","A story of boy and his toys come to life.","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc") 

#print(toy_story.storyline)

avatar = Movie("Avatar","A marine on an alien Planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar.storyline)
# avatar.show_trailer()

three_idiots = Movie("3 Idiots","An engineers tale.","https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg","https://www.youtube.com/watch?v=K0eDlFX9GMc")

#three_idiots.show_trailer()

school_of_rock = Movie("School of Rock","Rock music for learning","https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = Movie("Ratatouille","Rat becomes a chef","http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg","https://www.youtube.com/watch?v=3YG4h5GbTqU")

midnigt_in_paris = Movie("Midnight in Paris","Life in Paris After Midnight","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=FAfR8omt-CY")


movies = [toy_story,avatar,three_idiots,school_of_rock,ratatouille,midnigt_in_paris]

fresh_tomatoes.open_movies_page(movies)
