import math

from flask import render_template,request, redirect
from AppBanHang.dao import load_categories, load_products, count_products, authorize
from flask_login import login_user, logout_user
from AppBanHang import app,db, dao, login



@app.route('/')
def index():
    count = count_products()
    page_size = app.config['PAGE_SIZE']
    products = load_products(kw = request.args.get('kw'), cate_id = request.args.get('cate_id'),page = int(request.args.get('page',1)))
    return render_template('index.html', products = products, pages = math.ceil(count/page_size))


@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/logout')
def logout_view():
    logout_user()
    return redirect('login.html')

@app.route('/login',methods =['post'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')

    u = dao.authorize(username = username, password = password)
    if u:
        login_user(user = u)
    return redirect('/') if request.args.get('from') else redirect('/admin')


@app.route('/register')
def register_view():
    return render_template('register.html')

@app.context_processor
def common_responses():
    return {
        'categories': load_categories()
    }

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    with app.app_context():
        from AppBanHang import admin
        app.run(debug=True)
