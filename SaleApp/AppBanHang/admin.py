from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import Column

from AppBanHang.models import Category, Product, UserRoleEnum
from AppBanHang import app, db
from flask_login import logout_user , current_user
from flask import redirect

class AuthenticatedView(ModelView):
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN


class ProductView(AuthenticatedView):
    column_list = ['id', 'name','price','category_id']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    column_filters = ['id','name','price']

class BaseAuthenticatedView(BaseView):
    def is_accessible(self) -> bool:
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class StaticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/statics.html')

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        logout_user()
        return redirect('/admin')
    def is_accessible(self) -> bool:
        return current_user.is_authenticated

admin = Admin(app =app, name = "App's ADMIN")
admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(StaticsView(name="Thống Kê"))