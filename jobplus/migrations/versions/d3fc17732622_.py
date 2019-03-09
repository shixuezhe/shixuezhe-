"""empty message

Revision ID: d3fc17732622
Revises: 
Create Date: 2019-03-08 10:27:26.108400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3fc17732622'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('resume', sa.String(length=128), nullable=True),
    sa.Column('experience', sa.String(length=24), nullable=True),
    sa.Column('role', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('number', sa.String(length=48), nullable=False),
    sa.Column('slug', sa.String(length=64), nullable=True),
    sa.Column('address', sa.String(length=128), nullable=False),
    sa.Column('site', sa.String(length=64), nullable=True),
    sa.Column('logo', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=64), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('finance', sa.String(length=32), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.Column('staff_num', sa.String(length=32), nullable=True),
    sa.Column('location', sa.String(length=32), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_index(op.f('ix_company_slug'), 'company', ['slug'], unique=True)
    op.create_table('resume',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('age', sa.SmallInteger(), nullable=True),
    sa.Column('work_age', sa.SmallInteger(), nullable=True),
    sa.Column('home_city', sa.String(length=64), nullable=True),
    sa.Column('job_experience', sa.Text(), nullable=True),
    sa.Column('edu_experience', sa.Text(), nullable=True),
    sa.Column('project_experience', sa.Text(), nullable=True),
    sa.Column('resume_url', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('wage_low', sa.Integer(), nullable=False),
    sa.Column('wage_high', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=32), nullable=False),
    sa.Column('tags', sa.String(length=64), nullable=True),
    sa.Column('experience', sa.String(length=64), nullable=True),
    sa.Column('degree', sa.String(length=64), nullable=True),
    sa.Column('is_fulltime', sa.Boolean(), nullable=True),
    sa.Column('is_open', sa.Boolean(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery')
    op.drop_table('job')
    op.drop_table('resume')
    op.drop_index(op.f('ix_company_slug'), table_name='company')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###