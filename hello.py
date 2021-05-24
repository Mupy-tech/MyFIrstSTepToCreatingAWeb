from flask import Flask
#imported a flask class
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>HELLO world</p>"

@app.route("/hi")
def hiworld():
    return "<b>Hi world</b>"