from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://imdb236.p.rapidapi.com/api/imdb/most-popular-movies"

    headers = {
        "x-rapidapi-key": "fe1fafe432msh517b2ce221ff25ap135b06jsne7da14e55876",
        "x-rapidapi-host": "imdb236.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    movies = response.json()  # langsung list


    return render_template("index.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
