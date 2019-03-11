from flask import render_template,Blueprint,request,current_app
from jobplus.models import Job


job = Blueprint('job',__name__,url_prefix='/job')

@job.route('/')
def index():
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.order_by(Job.created_at.desc()).paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('job/index.html',pagination=pagination,active='job')

@job.route('/<int:job_id>/detail')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('job/detail.html',job=job)
