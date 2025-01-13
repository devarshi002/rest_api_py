from flask import Flask
app = Flask(__name__)

#decorators
@app.route("/")
def welcome():
    return "Henlo"

@app.route("/home")
def home():
    return "This is home page"


if __name__ == '__main__':
    app.run(debug=True)