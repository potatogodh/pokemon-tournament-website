from flask import Flask, render_template
import random
from pokemon_list import pokemon_list

app = Flask(__name__)

@app.route("/")
def index():
    random.shuffle(pokemon_list)
    return render_template("index.html", pokemon=pokemon_list)

if __name__ == "__main__":
    app.run()
