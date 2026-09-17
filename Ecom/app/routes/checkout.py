from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models import CartItem, Order, OrderItem

checkout = Blueprint("checkout", __name__)

@checkout.route("/checkout")
@login_required
def checkout_page():
    items = CartItem.query.filter_by(customer_id=current_user.id).all()
    if not items:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("cart.view_cart"))
    subtotal = sum(item.product.price * item.quantity for item in items)
    tax = round(subtotal * 0.08, 2)
    total = subtotal + tax
    return render_template("checkout/checkout.html", items=items, subtotal=subtotal, tax=tax, total=total, customer=current_user)

@checkout.route("/checkout/buy-now/<int:product_id>")
@login_required
def buy_now_checkout(product_id):
    from ..models import Product
    product = Product.query.get_or_404(product_id)
    subtotal = product.price
    tax = round(subtotal * 0.08, 2)
    total = subtotal + tax
    return render_template("checkout/checkout.html",
        items=[type('obj', (object,), {'product': product, 'quantity': 1})()],
        subtotal=subtotal, tax=tax, total=total,
        buy_now_product_id=product_id,
        customer=current_user
    )

@checkout.route("/checkout/save-shipping", methods=["POST"])
@login_required
def save_shipping():
    current_user.ship_first_name = request.form.get("first_name", "")
    current_user.ship_last_name = request.form.get("last_name", "")
    current_user.ship_address = request.form.get("address", "")
    current_user.ship_city = request.form.get("city", "")
    current_user.ship_state = request.form.get("state", "")
    current_user.ship_zip = request.form.get("zip_code", "")
    db.session.commit()
    return "", 204

@checkout.route("/checkout/place-order", methods=["POST"])
@login_required
def place_order():
    from ..models import Product
    buy_now_id = request.form.get("buy_now_product_id", type=int)

    if buy_now_id:
        product = Product.query.get_or_404(buy_now_id)
        if product.stock < 1:
            flash(f"Not enough stock for {product.name}.", "danger")
            return redirect(url_for("checkout.buy_now_checkout", product_id=buy_now_id))
        subtotal = product.price
        tax = round(subtotal * 0.08, 2)
        total = subtotal + tax
        order = Order(customer_id=current_user.id, total=total, status="Pending")
        db.session.add(order)
        db.session.flush()
        db.session.add(OrderItem(
            order_id=order.id,
            product_id=product.id,
            quantity=1,
            price=product.price
        ))
        product.stock -= 1
        db.session.commit()
        flash(f"Order #{order.id} placed successfully!", "success")
        return redirect(url_for("checkout.order_confirmation", order_id=order.id))

    items = CartItem.query.filter_by(customer_id=current_user.id).all()
    if not items:
        flash("Your cart is empty.", "warning")
        return redirect(url_for("cart.view_cart"))

    for item in items:
        if item.product.stock < item.quantity:
            flash(f"Not enough stock for {item.product.name}.", "danger")
            return redirect(url_for("cart.view_cart"))

    subtotal = sum(item.product.price * item.quantity for item in items)
    tax = round(subtotal * 0.08, 2)
    total = subtotal + tax

    order = Order(customer_id=current_user.id, total=total, status="Pending")
    db.session.add(order)
    db.session.flush()

    for item in items:
        db.session.add(OrderItem(
            order_id=order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.product.price
        ))
        item.product.stock -= item.quantity
        db.session.delete(item)

    db.session.commit()
    flash(f"Order #{order.id} placed successfully!", "success")
    return redirect(url_for("checkout.order_confirmation", order_id=order.id))

@checkout.route("/order/<int:order_id>")
@login_required
def order_confirmation(order_id):
    order = Order.query.get_or_404(order_id)
    if order.customer_id != current_user.id:
        flash("Unauthorized.", "danger")
        return redirect(url_for("main.home"))
    return render_template("checkout/confirmation.html", order=order)

@checkout.route("/orders")
@login_required
def order_history():
    orders = Order.query.filter_by(customer_id=current_user.id).order_by(Order.date_ordered.desc()).all()
    return render_template("checkout/orders.html", orders=orders)
