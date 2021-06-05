from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from . import db
from .models import User, Restaurant, Menu, MenuItem

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
    return render_template('restaurants.html', restaurants=restaurants)

@main.route('/new_restaurants')
@login_required
def new_restaurants():
    return render_template('new-restaurant.html')


@main.route('/restaurants', methods=['POST'])
@login_required
def restaurants_post():
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    menuName= request.form.get('menuName')
    menuDescription= request.form.get('menuDescription')

    exist = Restaurant.query.filter_by(name=name).first()

    if exist: 
        flash('Restaurant Name already exists')
        return redirect(url_for('main.restaurants'))

    new_menu = Menu(name=menuName, description=menuDescription)
    db.session.add(new_menu)
    db.session.commit()
    
    new_restaurant = Restaurant(name=name, owner=current_user.id, phone=phone, address=address, menu=new_menu.id)
    db.session.add(new_restaurant)
    db.session.commit()

    menuItemName= request.form.get('menuItemName')
    menuItemDescription= request.form.get('menuItemDescription')
    menuItemPrice = request.form.get('meuItemPrice')

    new_menu_item = MenuItem(name=menuItemName, description=menuItemDescription, price=menuItemPrice, menu=new_menu.id)
    db.session.add(new_restaurant)
    db.session.commit()

    return redirect(url_for('main.restaurants'))
