from flask import Blueprint, render_template
from flask_login import login_required, current_user

from . import db
from .models import User, Restaurant

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/restaurants')
@login_required
def restaurants():
    restaurants = Restaurant.query.all()
    return render_template('restaurants.html', name=current_user.name, restaurants=restaurants)


@main.route('/restaurants', methods=['POST'])
@login_required
def restaurants_post():
    name = request.form.get('name')

    exist = Restaurant.query.filter_by(name=name).first()

    if exist: 
        flash('Restaurant Name already exists')
        return redirect(url_for('main.restaurants'))

    new_restaurant = Restaurant(name=name, owner=current_user)

    db.session.add(new_restaurant)
    db.session.commit()

    return redirect(url_for('main.profile'))
