import os

from flask import Blueprint, render_template, request, session, url_for, redirect

from flask_advanced.add_forms import ProductForm
from flask_advanced.utils import add_data, get_data

product = Blueprint('product', __name__, template_folder='templates', static_folder='static1')

path_data_products = "blueprint/Products/data.json"
path_static_products = "blueprint/Products/static1"
DB1 = get_data(path_data_products)


@product.route('/products', methods=['GET'])
def get_products():
    return render_template('all_products.html', products=get_data(path_data_products))


@product.route('/products', methods=['POST'])
def search_products():
    id_product = request.form.get('id')
    price = request.form.get('price')
    data = []
    for i_product in get_data(path_data_products):
        if i_product['id'] == id_product and i_product['price'] == price:
            session[i_product['id']] = True
            return render_template('all_products.html', products=i_product, link_flags=session)
        elif i_product['price'] == price:
            session[i_product['price']] = True
            data.append(i_product)
        elif i_product['id'] == id_product:
            session[i_product['id']] = True
            data.append(i_product)
    return render_template('all_products.html', products=data, link_flags=session)


@product.route('/<name_product>', methods=['GET'])
def get_product(name_product):
    for i_product in get_data(path_data_products):
        if i_product['name'] == name_product:
            return render_template("product.html", product=i_product)
    else:
        return redirect(url_for('product.get_products'))


@product.route('/add_product', methods=['GET'])
def add_product():
    form_product = ProductForm()
    return render_template('add_product.html', form=form_product)


@product.route('/add_product', methods=['POST'])
def add_product_post():
    form_product = ProductForm()
    new_product = {"id": form_product.id, "name": request.form.get('name'),
                   "description": request.form.get('description'), "price": request.form.get('price')}
    image = request.files['image']
    if int(new_product['price']) < 0:
        return render_template('base.html', text_error="price entered incorrectly")
    new_product["img_name"] = image.filename
    path = os.path.join(path_static_products, image.filename)
    image.save(path)
    DB1.append(new_product)
    add_data(DB1, path_data_products)
    return redirect(url_for('product.get_products'))
