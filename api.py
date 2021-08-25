from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

USERS = ["Mato", "Peto", "Palo", "Martina", "Alexandra", "Jozko", "Klara"]
MOVIES = {
    "Harry Potter": datetime.fromtimestamp(1629468825), 
    "Herkules": datetime.fromtimestamp(1629526425), 
    "Mulan": datetime.fromtimestamp(1629872025), 
    "Sherlock Holmes": datetime.fromtimestamp(1629886425),
}
DESCRIPTIONS = {
    "Harry Potter": {
        "zaner": "Fantasy",
        "predloha": "J.K Rowling",
        "scenar": "Steve Kloves",
        "hudba": "John Williams",
        "ucinkujuci": "Daniel Radcliffe, Rupert Grint, Emma Watson, Robbie Coltrane",
        "hodnotenie": 79, 
    },
    "Herkules": {
        "zaner": "Rozpravka, Animovany",
        "predloha": "",
        "scenar": "Don McEnery",
        "hudba": "Alan Menken",
        "ucinkujuci": "Tate Donovan, Danny DeVito, James Woods",
        "hodnotenie": 79,
    },
    "Mulan": {
        "zaner": "Rozpravka, Animovany",
        "predloha": "",
        "scenar": "Barry Cook, Tony Bancroft",
        "hudba": "Jerry Goldsmith",
        "ucinkujuci": "Ming-Na Wen, BD Wong, Soon-tek Oh, Eddie Murphy",
        "hodnotenie": 84,
    },
    "Sherlock Holmes": {
        "zaner": "Dobrodruzny, Mysteriozny",
        "predloha": "Arthur Conan Doyle",
        "scenar": "Michael Robert Johnson, Anthony Peckham",
        "hudba": "Hans Zimmer",
        "ucinkujuci": "Robert Downey Jr., Jude Law, Rachel McAdams, Mark Strong, Eddie Marsan",
        "hodnotenie": 80,
    },
}
# TODO: dict of movies and users is missing
# TODO: no users found

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/time")
def get_time():
    return str(datetime.now())

@app.route("/<name>")
def get_user_id(name):
    if name in USERS:
        identification = USERS.index(name)
        return str(identification)
    return str(-1)

@app.route("/<name>/shopping-cart")
def get_shopping_cart(name):
    pass

# Change some data
@app.route("/change-name/<name>", methods=['POST'])
def change_name(name):
    # TODO: pridaj error pre zmenu hlasky v return
    current_name = request.form["username"]
    if current_name in USERS:
        identification = USERS.index(current_name)
        if request.form["newName"] != "":
            USERS[identification] = request.form["newName"]
            return "Username changed"
        return "New name is empty, please fill the form correctly"
    return "???"

# Get movies that are accessible for particular user
@app.route("/<name>/movies")
def get_movies(name):
    # TODO: implement dict of username to access movies
    return MOVIES

@app.route("/beautiful-movies")
def beautiful_movies():
    output = {}
    for key, value in MOVIES.items():
        output[key] = DESCRIPTIONS[key]
    return output



# FIXME: no security is implemented on API, anyone can use it, anyone can stole any username/change it, list the shopping cart or so!!
