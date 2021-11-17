from flask import Flask, request, Response
import json

app = Flask(__name__)

animal_management = {
    "1": { 'name': 'Arabian Oryx', 'date_admitted': '2021' },
    "2": { 'name': 'Przewalskis Horse','date_admitted': '2019' },
    "3": { 'name': 'California Condor', 'date admitted': '2018' }
}


@app.route("/")
def Zoo():
    return "Victor's Zoo is a great place"

@app.route("/animals")
def animals():
    html_response = "<ul>"
    for m in animal_management:
        html_response += "<li>" +  "<a href'/animal/" + m + "'>" + animal_management[m]["name"] + "</a>" + "</li>"
    return html_response


# READ
@app.route("/animal/<animal_id>")
def get_animal(animal_id):
    return json.dumps(animal_management[animal_id])

# CREATE    -POST
@app.route("/animal/add", methods=['POST]'])
def add_animal():
    req_data = request.get_json()
    animal = req_data['animal']     # {name: "something" ,date admitted: "something" } 

    new_animal = {"4" : animal }
    animal_management.update(new_animal)
    return "Animal was admitted succesfully"

if __name__ == "__main__":
    app.run(host='127.0.01')


### new animal
# { "movie" : { "name" : Corroboree Frog", "date_admitted" : "2021"} }



# READ      - GET
# UPDATE    - PUT
# DELETE    - GET


#https://medium.com/taronga-conservation-society-australia/10-endangered-species-saved-from-extinction-by-zoos-682c454d0125