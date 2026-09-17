from flask import Flask
from .extensions import db, login_manager, migrate
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.admin import admin
    from app.routes.cart import cart
    from app.routes.products import products
    from app.routes.checkout import checkout

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(cart)
    app.register_blueprint(products)
    app.register_blueprint(checkout)

    return app
