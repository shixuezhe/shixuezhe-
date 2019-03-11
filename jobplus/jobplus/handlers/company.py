from flask import Blueprint,render_template,redirect,flash,url_for,request,current_app
from jobplus.models import User,Company,Job,db
from jobplus.forms import CompanyProfileForm,JobForm
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

@company.route('/<int:company_id>/')
def detail(company_id):
    company = Company.query.get_or_404(company_id)
    return render_template('company/detail.html',company_id=company_id)

@company.route('/<int:company_id>/online_jobs')
def online_job(company_id):
    job = Job.query.filter_by(company_id=company_id).all()
    return render_template(company/online_job.html,company_id=company_id,active='online_job',job=job)

@company.route('/<int:company_id>/manage')
@company_required
def manage(company_id):
    company = Company.query.filter_by(users_id=company_id).first()
    return render_template('company/manage.html',company=company,active='manage')

@company.route('/<int:company_id>/manage/job')
@company_required
def manage_job(company_id):
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.filter_by(company_id=company_id).paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('company/manage_job.html',pagination=pagination,company_id=company_id)

@company.route('/<int:company_id>/manage/job/create',methods=['GET','POST'])
@company_required
def job_create(company_id):
    form = JobForm()
    if form.validate_on_submit():
        form.create_job(company_id)
        flash('职位创建成功','success')
        return redirect(url_for('company.manage_job',company_id=company_id))
    return render_template('company/job_create.html',form=form,company_id=company_id)

@company.route('/<int:company_id>/manage/job/edit',methods=['GET','POST'])
@company_required
def job_edit(company_id):
    job = Job.query.filter_by(company_id=company_id).first()
    form = JobForm(obj=job)
    if form.validate_on_submit():
        form.update_job(job)
        flash('职位更新成功','success')
        return redirect(url_for('company.manage_job',company_id=company_id))
    return render_template('company/job_edit.html',form=form,company_id=company_id)

@company.route('/<int:company_id>/manage/job/delete',methods=['GET','POST'])
@company_required
def job_delete(company_id):
    job = Job.query.filter_by(company_id=company_id).first()
    db.session.delete(job)
    db.session.commit()
    flash('职位删除成功','success')
    return redirect(url_for('company.manage_job',company_id=company_id))

@company.route('/profile',methods=['GET','POST'])
@login_required
def companyprofile():
    form = CompanyProfileForm(obj=current_user)
    form.name.data = current_user.username
    form.email.data = current_user.email
    if form.validate_on_submit():
        form.update_company(current_user)
        flash('个人信息更新成功','success')
        return redirect(url_for('front.index'))
    return render_template('company/companyprofile.html',form=form)


