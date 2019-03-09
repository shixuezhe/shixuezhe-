from flask import Blueprint,render_template,redirect,flash,url_for,request,current_app
from jobplus.models import User,Company,Job
from jobplus.forms import CompanyProfileForm
from jobplus.decorators import company_required
from flask_login import login_required,current_user

company = Blueprint('company',__name__,url_prefix = '/company')

@company.route('/')
def index():
    page = request.args.get('page',default=1,type=int)
    pagination = Company.query.order_by(Company.created_at.desc()).paginate(
        page=page,
        per_page=current_app.config['COMPANY_PER_PAGE'],
        error_out=False
    )
    return render_template('company/index.html',pagination=pagination,active='company')

@company.route('/manage')
@company_required
def manage():
    return render_template('company/manage.html')

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



