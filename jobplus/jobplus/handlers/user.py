from flask import Blueprint,render_template,redirect,flash,url_for
from jobplus.models import User
from jobplus.forms import UserProfileForm
from flask_login import login_required,current_user

user=Blueprint('user',__name__,url_prefix='/user')

@user.route('/profile',methods=['GET','POST'])
@login_required
def userprofile():
    form=UserProfileForm(obj=current_user)
    if form.validate_on_submit():
        form.update_user(current_user)
        flash('个人信息更新成功','success')
        return redirect(url_for('front.index'))
    return render_template('user/userprofile.html',form=form)



