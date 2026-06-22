from flask import Flask, render_template, request, jsonify
import random
from pokemon_by_gen import pokemon_by_gen

app = Flask(__name__)

gen_winners = {}  # store winners of each generation


@app.route("/")
def home():
    return render_template("select_gen.html")


@app.route("/tournament/<int:gen>")
def tournament(gen):
    pokemon = pokemon_by_gen.get(gen, [])
    random.shuffle(pokemon)
    return render_template("index.html", pokemon=pokemon, gen=gen)


@app.route("/save_winner", methods=["POST"])
def save_winner():
    data = request.json
    gen = data["gen"]
    winner = data["winner"]
    gen_winners[gen] = winner
    return jsonify({"status": "saved"})


@app.route("/champions")
def champions():
    # Only allow if at least 2 gens completed
    if len(gen_winners) < 2:
        return "Not enough generation winners yet."

    final_list = list(gen_winners.values())
    random.shuffle(final_list)
    return render_template("champions.html", pokemon=final_list)


if __name__ == "__main__":
    app.run(debug=True)

