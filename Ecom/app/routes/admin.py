from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from ..extensions import db
from ..models import Product, Order, Customer
from functools import wraps

admin = Blueprint("admin", __name__)

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            flash("Admin access required.", "danger")
            return redirect(url_for("main.home"))
        return f(*args, **kwargs)
    return decorated

@admin.route("/admin")
@login_required
@admin_required
def dashboard():
    from ..models import OrderItem
    products = Product.query.all()
    orders = Order.query.order_by(Order.date_ordered.desc()).all()
    customers = Customer.query.all()
    total_sales = db.session.query(
        db.func.sum(OrderItem.price * OrderItem.quantity)
    ).scalar() or 0
    return render_template("admin/dashboard.html", products=products, orders=orders, customers=customers, total_sales=total_sales)

@admin.route("/admin/products/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        stock = request.form.get("stock")
        image = request.form.get("image")

        if not name or not description or not price or not stock:
            flash("All fields except image are required.", "danger")
            return redirect(url_for("admin.add_product"))

        try:
            price = float(price)
            stock = int(stock)
        except ValueError:
            flash("Price must be a number and stock must be an integer.", "danger")
            return redirect(url_for("admin.add_product"))
        
        product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image or '',
            category=request.form.get('category', 'Other')
            )
        db.session.add(product)
        db.session.commit()
        flash(f"Product '{name}' added.", "success")
        return redirect(url_for("admin.dashboard"))
        
    return render_template("admin/product_form.html", product=None)

@admin.route("/admin/products/edit/<int:product_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == "POST":
        product.name = request.form.get("name")
        product.description = request.form.get("description")
        try:
            product.price = float(request.form.get("price"))
            product.stock = int(request.form.get("stock"))
        except ValueError:
            flash("Invalid input for price or stock.", "danger")
            return redirect(url_for("admin.edit_product", product_id=product.id))
        product.image = request.form.get("image") or ''
        product.category = request.form.get("category", "Other")
        db.session.commit()
        flash(f"Product '{product.name}' updated.", "success")
        return redirect(url_for("admin.dashboard"))
    
    

    return render_template("admin/product_form.html", product=product)

@admin.route("/admin/products/delete/<int:product_id>", methods=["POST"])
@login_required
@admin_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash(f"Product '{product.name}' deleted.", "success")
    return redirect(url_for("admin.dashboard"))
