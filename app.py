from flask import Flask, render_template
import requests 
import random

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://imdb236.p.rapidapi.com/api/imdb/most-popular-movies"
    headers = {
        "x-rapidapi-key": "fe1fafe432msh517b2ce221ff25ap135b06jsne7da14e55876",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    all_movies = response.json()  # langsung list

    return render_template('home.html', movies=all_movies)

@app.route('/movies')
def movies():
    url = "https://imdb236.p.rapidapi.com/api/imdb/most-popular-movies"
    headers = {
        "x-rapidapi-key": "c9407e0263msh9289678d2a98828p120d30jsna3a30640cdfe",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    all_movies = response.json()  # langsung list

    return render_template('mostpopuler.html', movies=all_movies)

if __name__ == '__main__':
    app.run(debug=True)
