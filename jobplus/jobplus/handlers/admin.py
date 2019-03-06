from flask import render_template,Blueprint,request,current_user,flash,url_for
from jobplus.decorators import admin_required
from jobplus.models import User,db

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')
