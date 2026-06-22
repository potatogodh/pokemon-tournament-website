from flask import Flask, render_template
import random
from pokemon_list import pokemon_list

app = Flask(__name__)

@app.route("/")
def index():
    # Shuffle once and send to frontend
    shuffled = pokemon_list[:]
    random.shuffle(shuffled)
    return render_template("index.html", pokemon=shuffled)

if __name__ == "__main__":
    app.run(debug=True)
