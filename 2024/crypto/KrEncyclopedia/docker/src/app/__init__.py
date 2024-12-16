from flask import Flask
import random
import string 
import requests

def getKey():

    alph = [c for c in string.ascii_lowercase]
    unordedered = alph.copy() 

    random.shuffle(unordedered)

    return dict(zip(alph, unordedered))

def getFlag():
    flag = ''
    with open('flag.txt', 'r') as f:
        flag = f.readlines()[0][0:-1]
    return flag

def getArticles():
    def fetch_random_wikipedia_article():
        url = "https://en.wikipedia.org/w/api.php"

        params = {
            "format": "json",
            "action": "query",
            "generator": "random",
            "grnnamespace": 0,
            "prop": "extracts",
            "exchars": 4000,
            "explaintext": True
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            pages = data["query"]["pages"]

            for _, page_data in pages.items():
                return page_data["extract"]
                

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from Wikipedia: {e}")

    art = [fetch_random_wikipedia_article() for _ in range(0,10)]
    return art

def create_app():
    app = Flask(__name__)
    app.config['CIPHER_KEY'] = getKey()
    app.config['FLAG'] = getFlag()
    app.config['ARTICLES'] = getArticles()

    with app.app_context():
        from . import routes

    return app
