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
        "x-rapidapi-key": "fe1fafe432msh517b2ce221ff25ap135b06jsne7da14e55876",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # Pastikan data yang dipassing ke template adalah list film
    movies = response.json() # tergantung struktur JSON response
    return render_template('index.html', movies=movies)

@app.route('/genres')
def genres():
    url = "https://imdb236.p.rapidapi.com/api/imdb/genres"
    headers = {
        "x-rapidapi-key": "fe1fafe432msh517b2ce221ff25ap135b06jsne7da14e55876",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    genre_list = response.json()  # pastikan ini sesuai struktur JSON API kamu

    return render_template("genres.html", genres=genre_list)




if __name__ == '__main__':
    app.run(debug=True)
