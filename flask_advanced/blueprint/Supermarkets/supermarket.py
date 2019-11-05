import os
import uuid

from flask import Blueprint, render_template, request, session, url_for, redirect

from .utils import get_data, add_data

supermarket = Blueprint("supermarket", __name__, template_folder='templates', static_folder='static2')

data_supermarkets = get_data()


@supermarket.route('/supermarkets', methods=['GET'])
def get_supermarkets():
    return render_template('all_supermarkets.html', supermarkets=get_data())


@supermarket.route('/supermarkets', methods=['POST'])
def search_supermarkets():
    id_supermarket = request.form.get('id')
    location = request.form.get('location')
    data = []
    for i in get_data():
        if i['id'] == id_supermarket and i['location'] == location:
            session[i['id']] = True
            return render_template('all_supermarkets.html', supermarkets=i, link_flags=session)
        elif i['location'] == location:
            session[i['location']] = True
            data.append(i)
        elif i['id'] == id_supermarket:
            session[i['id']] = True
            data.append(i)
    return render_template('all_supermarkets.html', supermarkets=data, link_flags=session)


@supermarket.route('/<name_supermarket>', methods=['GET'])
def get_supermarket(name_supermarket):
    for i in get_data():
        if i["name"] == name_supermarket:
            return render_template('supermarket.html', supermarket=i)


@supermarket.route('/add_supermarket', methods=['GET'])
def add_supermarket():
    return render_template('add_supermarket.html')


@supermarket.route('/add_supermarket', methods=['POST'])
def add_supermarket_post():
    new_supermarket = {"id": str(uuid.uuid4()), "name": request.form.get('name'),
                       "location": request.form.get('location')}
    image = request.files['image']
    new_supermarket["img_name"] = image.filename
    path = os.path.join('blueprint/Supermarkets/static2', image.filename)
    image.save(path)
    data_supermarkets.append(new_supermarket)
    add_data(data_supermarkets)
    return redirect(url_for('supermarket.get_supermarkets'))


