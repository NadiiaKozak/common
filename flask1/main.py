from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/home')
def get_home_page():
    return render_template('home.html')

@app.route('/vegetables')
def get_vegetables_page():
    vagetables = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', list_vagetables=vagetables)

@app.route('/fruits')
def get_fruits_page():
    fruits = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', list_fruits=fruits)

if __name__ == "__main__":
    app.run(debug=True)

