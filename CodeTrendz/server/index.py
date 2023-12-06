from flask import Flask, render_template
from ..scripts.etl import ExtractAndRun

app = Flask(__name__)
etl = ExtractAndRun()


@app.route("/")
def hello_world():
    return "<p>Hello world</p>"


@app.route("/topic-modelling")
def topic_modelling():
    etl.run()
    return render_template("scripts/data/vis_data.html")


if __name__ == "__main__":
    app.run(debug=True)
