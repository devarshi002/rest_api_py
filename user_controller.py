from flask import Blueprint

# Create a Blueprint instance
user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/signup')
def signup():
    return "Agaya be finally"
