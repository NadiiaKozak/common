from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)

@app.route('/home')
def get_home_page():
    return render_template("home.html")

@app.route('/visa')
def get_visa_page():
    return render_template("visa.html", data=get_data())

@app.route('/mastercard')
def get_mastercard_page():
    return render_template("mastercard.html", data=get_data())

@app.route('/american_express')
def get_american_express_page():
    return render_template("american_express.html", data=get_data())

@app.route('/maestro')
def get_maestro_page():
    return render_template("maestro.html", data=get_data())

@app.route('/paypal')
def get_paypal_page():
    return render_template("paypal.html", data=get_data())

@app.route('/discover')
def get_discover_page():
    return render_template("discover.html", data=get_data())

@app.route('/author')
def get_author_page():
    return render_template("author.html")


if __name__ == "__main__":
    app.run(debug=True)
