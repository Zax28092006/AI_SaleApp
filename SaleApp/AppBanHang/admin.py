from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column

from AppBanHang.models import Category, Product
from AppBanHang import app, db

class ProductView(ModelView):
    column_list = ['id', 'name','price','category_id']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    column_filters = ['id','name','price']

class StaticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('adminLayoutadmin/statics.html')
admin = Admin(app =app, name = "App's ADMIN")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StaticsView(name="Thống Kê"))