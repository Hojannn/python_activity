from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from ..extensions import db
from ..models import Customer

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("full_name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if not username or not email or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("auth.register"))

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("auth.register"))

        if Customer.query.filter_by(email=email).first():
            flash("Email already registered.", "danger")
            return redirect(url_for("auth.register"))

        new_user = Customer(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            is_admin=email == ADMIN_EMAIL
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash("Welcome to TECH-CORE!", "success")
        return redirect(url_for("main.home"))

    return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = Customer.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))

        login_user(user)
        next_page = request.args.get('next')
        if next_page and '/cart/add' not in next_page and '/cart/buy-now' not in next_page:
            return redirect(next_page)
        return redirect(url_for("main.home"))

    return render_template("auth/login.html")





@auth.route("/account")
@login_required
def account():
    from ..models import Order
    orders = Order.query.filter_by(customer_id=current_user.id).order_by(Order.date_ordered.desc()).limit(5).all()
    return render_template("accounts/account_details.html", orders=orders)


@auth.route("/account/update", methods=["POST"])
@login_required
def update_account():
    username = request.form.get("username")
    email = request.form.get("email")

    if not username or not email:
        flash("Name and email cannot be empty.", "danger")
        return redirect(url_for("auth.account"))

    existing = Customer.query.filter_by(email=email).first()
    if existing and existing.id != current_user.id:
        flash("Email already in use by another account.", "danger")
        return redirect(url_for("auth.account"))

    current_user.username = username
    current_user.email = email
    db.session.commit()
    flash("Account updated successfully.", "success")
    return redirect(url_for("auth.account"))


@auth.route("/reset-password", methods=["GET", "POST"])
def reset_password():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm_password")

        if not username or not password:
            flash("All fields are required.", "danger")
            return redirect(url_for("auth.reset_password"))

        if password != confirm:
            flash("Passwords do not match.", "danger")
            return redirect(url_for("auth.reset_password"))

        user = Customer.query.filter_by(username=username).first()
        if not user:
            flash("No account found with that username.", "danger")
            return redirect(url_for("auth.reset_password"))

        user.password_hash = generate_password_hash(password)
        db.session.commit()
        flash("Password reset successfully. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/reset_password.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
