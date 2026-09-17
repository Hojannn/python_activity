from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models import CartItem, Product

cart = Blueprint("cart", __name__)

@cart.route("/cart")
@login_required
def view_cart():
    items = CartItem.query.filter_by(customer_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in items)
    return render_template("cart/cart.html", items=items, total=total)

@cart.route("/cart/add/<int:product_id>", methods=["GET", "POST"])
def add_to_cart(product_id):
    if not current_user.is_authenticated:
        flash("Please log in to add items to your cart.", "warning")
        return redirect(url_for("auth.login"))
    if request.method == "GET":
        return redirect(url_for("auth.login"))
    product = Product.query.get_or_404(product_id)
    item = CartItem.query.filter_by(customer_id=current_user.id, product_id=product_id).first()
    if item:
        item.quantity += 1
    else:
        item = CartItem(customer_id=current_user.id, product_id=product_id, quantity=1)
        db.session.add(item)
    db.session.commit()
    flash(f"{product.name} added to cart.", "success")
    return redirect(url_for("products.all_products"))

@cart.route("/cart/buy-now/<int:product_id>", methods=["GET", "POST"])
def buy_now(product_id):
    if not current_user.is_authenticated:
        flash("Please log in to continue.", "warning")
        return redirect(url_for("auth.login"))
    if request.method == "GET":
        return redirect(url_for("auth.login"))
    Product.query.get_or_404(product_id)
    return redirect(url_for("checkout.buy_now_checkout", product_id=product_id))


@cart.route("/cart/remove/<int:item_id>", methods=["POST"])
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.customer_id != current_user.id:
        flash("Unauthorized.", "danger")
        return redirect(url_for("cart.view_cart"))
    db.session.delete(item)
    db.session.commit()
    flash("Item removed.", "success")
    return redirect(url_for("cart.view_cart"))

@cart.route("/cart/update/<int:item_id>/<action>", methods=["POST"])
@login_required
def update_quantity(item_id, action):
    item = CartItem.query.get_or_404(item_id)
    if item.customer_id != current_user.id:
        return redirect(url_for("cart.view_cart"))
    if action == "increase":
        item.quantity += 1
    elif action == "decrease":
        if item.quantity > 1:
            item.quantity -= 1
        else:
            db.session.delete(item)
            db.session.commit()
            return redirect(url_for("cart.view_cart"))
    db.session.commit()
    return redirect(url_for("cart.view_cart"))
