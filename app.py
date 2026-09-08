from flask import Flask, render_template
import json

app = Flask(__name__)


def load_trains():
    with open("trains.json", "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def index():
    trains = load_trains()
    return render_template("index.html", trains=trains)


if __name__ == "__main__":
    app.run(debug=True)