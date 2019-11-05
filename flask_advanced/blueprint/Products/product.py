import os
import uuid

from flask import Blueprint, render_template, request, session, url_for, redirect


from .utils import get_data, add_data

product = Blueprint('product', __name__, template_folder='templates', static_folder='static1')

DB1 = get_data()


@product.route('/products', methods=['GET'])
def get_products():
    return render_template('all_products.html', products=get_data())


@product.route('/products', methods=['POST'])
def search_products():
    id_product = request.form.get('id')
    price = request.form.get('price')
    data = []
    for i in get_data():
        if i['id'] == id_product and i['price'] == price:
            session[i['id']] = True
            return render_template('all_products.html', products=i, link_flags=session)
        elif i['price'] == price:
            session[i['price']] = True
            data.append(i)
        elif i['id'] == id_product:
            session[i['id']] = True
            data.append(i)
    return render_template('all_products.html', products=data, link_flags=session)


@product.route('/<name_product>', methods=['GET'])
def get_product(name_product):
    for i in get_data():
        if i['name'] == name_product:
            return render_template("product.html",
                                   picture=i['img_name'],
                                   title=i['name'],
                                   text=i['description'],
                                   price=i['price'],
                                   id_product=i['id'])
    else:
        return redirect(url_for('product.get_products'))



@product.route('/add_product', methods=['GET'])
def add_product():
    return render_template('add_product.html')


@product.route('/add_product', methods=['POST'])
def add_product_post():
    new_product = {"id": str(uuid.uuid4()), "name": request.form.get('name'),
                   "description": request.form.get('description'), "price": request.form.get('price')}
    image = request.files['image']
    new_product["img_name"] = image.filename
    path = os.path.join('blueprint/Products/static1', image.filename)
    image.save(path)
    DB1.append(new_product)
    add_data(DB1)
    return redirect(url_for('product.get_products'))


