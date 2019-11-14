import os
import uuid

from flask import Blueprint, render_template, request, session, url_for, redirect

from flask_advanced.add_forms import SupermarketForm
from flask_advanced.utils import get_data, add_data

supermarket = Blueprint("supermarket", __name__, template_folder='templates', static_folder='static2')

path_data_supermarkets = "blueprint/Supermarkets/data.json"
path_static_supermarkets = "blueprint/Supermarkets/static2"

data_supermarkets = get_data(path_data_supermarkets)


@supermarket.route('/s/supermarkets', methods=['GET'])
def get_supermarkets():
    return render_template('all_supermarkets.html', supermarkets=get_data(path_data_supermarkets))


@supermarket.route('/s/supermarkets', methods=['POST'])
def search_supermarkets():
    id_supermarket = request.form.get('id')
    location = request.form.get('location')
    data = []
    for i_supermarket in get_data(path_data_supermarkets):
        if i_supermarket['id'] == id_supermarket and i_supermarket['location'] == location:
            session[i_supermarket['id']] = True
            return render_template('all_supermarkets.html', supermarkets=i_supermarket,
                                   link_flags=session)
        elif i_supermarket['location'] == location:
            session[i_supermarket['location']] = True
            data.append(i_supermarket)
        elif i_supermarket['id'] == id_supermarket:
            session[i_supermarket['id']] = True
            data.append(i_supermarket)
    return render_template('all_supermarkets.html', supermarkets=data, link_flags=session)


@supermarket.route('/s/<name_supermarket>', methods=['GET'])
def get_supermarket(name_supermarket):
    for i_supermarket in get_data(path_data_supermarkets):
        if i_supermarket["name"] == name_supermarket:
            return render_template('supermarket.html', supermarket=i_supermarket)
    else:
        return redirect(url_for('supermarket.get_supermarkets'))


@supermarket.route('/s/add_supermarket', methods=['GET'])
def add_supermarket():
    form_supermarket = SupermarketForm()
    return render_template('add_supermarket.html', form=form_supermarket)


@supermarket.route('/s/add_supermarket', methods=['POST'])
def add_supermarket_post():
    new_supermarket = {"id": str(uuid.uuid4()), "name": request.form.get('name'),
                       "location": request.form.get('location')}
    image = request.files['image']
    new_supermarket["img_name"] = image.filename
    path = os.path.join(path_static_supermarkets, image.filename)
    image.save(path)
    data_supermarkets.append(new_supermarket)
    add_data(data_supermarkets, path_data_supermarkets)
    return redirect(url_for('supermarket.get_supermarkets'))


