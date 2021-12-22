# if we want to create routes for our app, we need access to our app
# import the app object we made
from app import app
# allow flask routes to load html pages with render_template()
from flask import render_template

# creating a route with a decorator that flask understands
@app.route('/')
def home():
    import requests as r
    data = r.get('https://pokeapi.co/api/v2/pokedex/hoenn')
    if data.status_code == 200:
        data = data.json()
        context={
            'name': data['name'].title(),
            'poke': data['pokemon_entries']
        }
    return render_template('index.html', **context)

#route for about page

@app.route('/about')
def about():
    context = {
        'teacher': 'Sam',
        'students': ['Zaki', 'Vanessa', 'Paul', 'Shaharima', 'Mohammed', 'Ezekiel', 'Adrian', 'Ethan']
    }
    # we're taking that context dictionary and unpacking it's k/v pairs into keyword arguments for the render template function
    # using **kwargs (keyword arguments)
    return render_template('about.html', classname='Foxes78', **context)
