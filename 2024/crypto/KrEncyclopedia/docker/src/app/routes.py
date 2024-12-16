from flask import current_app as app, render_template
import random

@app.route('/wiki', methods=['GET'])
def wiki():
    r = random.randint(0, 9) 
    randomArticle = app.config['ARTICLES'][r].lower()
    sanitized = list(filter(lambda ch: ch in app.config['CIPHER_KEY'], randomArticle))
    res = ''.join(list(map(lambda ch: app.config['CIPHER_KEY'][ch], sanitized)))

    return render_template('index.html', header="Free Wikipedia article of the Request!", content=res)

@app.route('/flag', methods=['GET'])
def flag():
    res = ''.join(list(map(lambda ch: app.config['CIPHER_KEY'][ch], app.config['FLAG'])))
    return render_template('index.html', header="Here is your free flag!", content=res)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', header="KrEncyclopedia", content="Detta är tjänsten för att sprida mitt oknäckbara chiffer!\n Jag har till och med inkluderat en tjänst som krypterar Wikipediaartiklar för att bevisa hur oläsliga de blir.")
