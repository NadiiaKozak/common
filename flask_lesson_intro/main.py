from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/home')
def get_home_page():
    return render_template("home.html")


@app.route('/visa')
def get_visa_page():
    picture = 'visa.jpg'
    title = 'Visa'
    for i in get_data():
        if i['title'] == title:
            return render_template("visa.html", picture=picture, title=title, text=i['text'] )


@app.route('/mastercard')
def get_mastercard_page():
    picture = 'mc.png'
    title = 'MasterCard'
    for i in get_data():
        if i['title'] == title:
            return render_template("mastercard.html", picture=picture, title=title, text=i['text'])


@app.route('/american_express')
def get_american_express_page():
    picture = 'american.jpg'
    title = 'American Express'
    for i in get_data():
        if i['title'] == title:
            return render_template("american_express.html", picture=picture, title=title, text=i['text'])


@app.route('/maestro')
def get_maestro_page():
    picture = 'maestro.jpeg'
    title = 'Maestro'
    for i in get_data():
        if i['title'] == title:
            return render_template("maestro.html", picture=picture, title=title, text=i['text'])


@app.route('/paypal')
def get_paypal_page():
    picture = 'paypal.jpg'
    title = 'PayPal'
    for i in get_data():
        if i['title'] == title:
            return render_template("paypal.html", picture=picture, title=title, text=i['text'])


@app.route('/discover')
def get_discover_page():
    picture = 'discover.jpeg'
    title = 'Discover'
    for i in get_data():
        if i['title'] == title:
            return render_template("paypal.html", picture=picture, title=title, text=i['text'])


@app.route('/author')
def get_author_page():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
