import math

from flask import render_template,request
from AppBanHang.dao import load_categories, load_products, count_products

from AppBanHang import app


@app.route('/')
def index():
    count = count_products()
    page_size = app.config['PAGE_SIZE']
    products = load_products(kw = request.args.get('kw'), cate_id = request.args.get('cate_id'),page = int(request.args.get('page',1)))
    return render_template('index.html', products = products, pages = math.ceil(count/page_size))


@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.context_processor
def common_responses():
    return {
        'categories': load_categories()
    }

if __name__ == '__main__':
    with app.app_context():
        from AppBanHang import admin
        app.run(debug=True)
