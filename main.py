from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie1 = get_random_movie()
    movie2 = get_random_movie()
    while movie2 == movie1:
        movie2 = get_random_movie()
    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie1 + "</li>"
    content += "</ul>"

    

    # TODO: pick another random movie, and display it under
    # the heading "<h1>Tommorrow's Movie</h1>"
    content += "<h1>Tomorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + movie2 + "</li>"
    content += "</ul>"
    return content


def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movie_list = ['Cold Mountain', 'Gone with the Wind', 'The Babadook', 'Star Wars: The Last Jedi', 'Avatar: The Last Airbender']
    # TODO: randomly choose one of the movies, and return it
    movie_selection_num = random.randrange(0,len(movie_list))
    
    movie_selection = movie_list[movie_selection_num]
    
    return movie_selection

    


app.run()
