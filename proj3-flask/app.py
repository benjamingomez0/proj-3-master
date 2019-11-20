# import flask
from flask import Flask

# import resources


# import models




DEBUG = True
PORT = 8000

app = Flask(__name__)



# create routes
@app.route('/')
def index():
    return 'hi'



# connect CORS to React



# register blueprints



if __name__ == '__main__':
    models.initialize()    
    app.run(debug=DEBUG, port=PORT)
