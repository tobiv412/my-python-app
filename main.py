from flask import Flask, request, Response
import json

app = Flask(__name__)

movie_db = {
    "1" : { 'name' : 'Stargate', 'release_date' : '1994' },
    "2" : { 'name' : 'Sunshine', 'release_date': '2007' },
    "3" : { 'name' : 'The Holiday', 'release_date': '2004'}
    }

@app.route("/")
def hello():
    return "Hello World"

@app.route("/hello")
def world():
    return "<h1>Hello World!!!!</h1>"

@app.route("/movie")
def get_movies():
    html_response = "<ul>"
    for m in movie_db:
        html_response += "<li>" + "<a href+' /movie/'" + m + ">" + movie_db[m] ["name"] + "</a>" + "</li>"
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
    return json.dumps(movie_db[movie_id])

if __name__ == "__main__":
    app.run(host='127.0.0.1')

#CRUD

# CREATE -POST
# READ   -GET
# UPDATE -PUT
# DELETE -GET