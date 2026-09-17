from flask import Blueprint, render_template, request
from ..models import Product

products = Blueprint('products', __name__)

CATEGORIES = ['CPU', 'GPU', 'Memory', 'Motherboard', 'Storage', 'Monitor', 'Power Supply', 'Peripherals']

@products.route('/products')
def all_products():
    query = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()
    page = request.args.get('page', 1, type=int)
    per_page = 20

    items = Product.query
    if query:
        items = items.filter(Product.name.ilike(f'%{query}%'))
    if category:
        items = items.filter(Product.category == category)

    pagination = items.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('products/products.html',
        products=pagination.items,
        pagination=pagination,
        query=query,
        category=category,
        categories=CATEGORIES
    )

@products.route('/products/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('products/prod_details.html', product=product)
