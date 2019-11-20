# import flask
from flask import Flask, g

# import resources


# import models
import models


DEBUG = True
PORT = 8000

app = Flask(__name__)


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


# create routes
@app.route('/')
def index():
    return 'hi'



# connect CORS to React



# register blueprints



if __name__ == '__main__':
    models.initialize()    
    app.run(debug=DEBUG, port=PORT)
