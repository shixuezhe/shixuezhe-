from flask import Blueprint,render_template,redirect,flash,url_for
from jobplus.models import User,Resume
from jobplus.forms import UserProfileForm,ResumeForm
from flask_login import login_required,current_user

user=Blueprint('user',__name__,url_prefix='/user')

@user.route('/profile',methods=['GET','POST'])
@login_required
def userprofile():
    form=UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.update_user(current_user)
        flash('个人信息更新成功','success')
        return redirect(url_for('user.home_page',user_id=current_user.id))
    return render_template('user/userprofile.html',form=form)

@user.route('/<int:user_id>/home',methods=['GET','POST'])
def home_page(user_id):
    resume = Resume.query.get_or_404(user_id)
    return render_template('user/home_page.html',resume=resume,user_id=user_id)

@user.route('/<int:user_id>/home/resume',methods=['GET','POST'])
@login_required
def resume(user_id):
    resume = Resume.query.get_or_404(user_id)
    form = ResumeForm()
    if form.validate_on_submit():
        form.update_resume(resume)
        flash('简历编辑成功','success')
        return redirect(url_for('user.home_page', user_id=user_id))
    return render_template('user/resume.html',form=form)


