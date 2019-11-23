from flask import Flask, render_template

from blueprint.Products.product import product
from blueprint.Supermarkets.supermarket import supermarket

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'super secret key'

app.register_blueprint(product)
app.register_blueprint(supermarket)


@app.route('/home')
def get_home_page():
    return render_template("home.html")


@app.errorhandler(404)
def page_non_found(error):
    return render_template('error_404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
