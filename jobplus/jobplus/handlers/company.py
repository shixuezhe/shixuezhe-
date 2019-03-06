from flask import Blueprint,render_template,redirect,flash,url_for
from jobplus.models import User
from jobplus.forms import CompanyProfileForm
from jobplus.decorators import company_required
from flask_login import login_required,current_user

company = Blueprint('company',__name__,url_prefix = '/company')

@company.route('/')
@company_required
def index():
    return render_template('company/index.html')


@company.route('/profile',methods=['GET','POST'])
@login_required
def companyprofile():
    form = CompanyProfileForm(obj=current_user)
    form.name.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.update_company(current_user)
        flash('个人信息更新成功','success')
        return redirect(url_for('company.index'))
    return render_template('company/companyprofile.html',form=form)



