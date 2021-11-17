from flask import Flask, request, Response
from flask.config import Config
from flask_sqlalchemy import SQLAlchemy
from config import Config
import json

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Movies(db,Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(lenght=255))
    release_year = db.Column(db.Integer)



@app.route("/")
def hello():
    return "Hello World"

@app.route("/hello")
def world():
    return "<h1>Hello World!!!!</h1>"

@app.route("/movie")
def get_movies():
    # RETRIEVE ALL MOVIES FROM TABLE MOVIES
    movies = Movies.query.all() 
    html_response = "<ul>"
    for m in movies:
        html_response += "<li>" + "<a href+' /movie/'" + str(m.id) + ">" + movie_db[m] ["name"] + "</a>" + "</li>"
        html_response += "</ul>"
    return html_response
    
    #return json.dumps (movie_db)

#CREATE  - POST
@app.route("/movie/add", methods=['POST'])
def add_movie(): #add_movies*** #changed_movies_to_movie
    req_data = request.get_json()
    movie = req_data['movie']        # { name: "something" , release_date: "something" 


    new_movie ={ "4" : movie }
    movie_db.update (new_movie)
    return "Movie was added successfully"


# READ 
@app.route("/<movie_id>")
def get_movie(movie_id):
    movie = Movies.query.get(movie_id) # SELECT
    return json.dumps(movie_db[movie_id])

if __name__ == "__main__":
    app.run(host='127.0.0.1')

#CRUD

# CREATE -POST
# READ   -GET
# UPDATE -PUT
# DELETE -GET