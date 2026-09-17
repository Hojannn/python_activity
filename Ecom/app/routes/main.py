from flask import Blueprint, render_template
from ..models import Product


main = Blueprint("main", __name__)



@main.route("/")
def home():
    products = Product.query.limit(8).all()
    return render_template("home.html", products=products)

@main.route('/home')
def home_page():
    return render_template("home.html")

@main.route('/login')
def login():
    return render_template("auth/login.html")

@main.route('/register')
def register():
    return render_template("auth/register.html")

@main.route('/about')
def about():
    return render_template("about.html")

@main.route('/contact')
def contact():
    return render_template("contact.html")