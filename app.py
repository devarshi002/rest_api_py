from flask import Flask
from user_controller import user_blueprint

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Henlo"

@app.route("/home")
def home():
    return "This is home page"

# Register the Blueprint
app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(debug=True)
