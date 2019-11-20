# import flask
from flask import Flask, g
from flask_login import LoginManager

# import resources


# import models
import models


DEBUG = True
PORT = 8000

login_manager = LoginManager()
app = Flask(__name__)

app.secret_key = "Type a string that is totally not this string here"
login_manager.init_app(app)


# create routes
@login_manager.user_loader
def load_user(userId):
    try:
        return models.User.get(models.User.id == userId)
    except models.DoesNotExist():
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response



# connect CORS to React



# register blueprints



if __name__ == '__main__':
    models.initialize()    
    app.run(debug=DEBUG, port=PORT)
