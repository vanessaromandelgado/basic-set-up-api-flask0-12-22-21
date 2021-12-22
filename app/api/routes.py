#setting up blueprint modularized connection with flask
#app needs to know how to connect with flask
from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

#flask decorator yay!
@api.route('/')
def test():
    return {'datadatadata': 'ooh look at this fancy data'}

