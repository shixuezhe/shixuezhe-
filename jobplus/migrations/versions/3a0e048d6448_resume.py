"""resume

Revision ID: 3a0e048d6448
Revises: d3fc17732622
Create Date: 2019-03-12 17:03:28.404281

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3a0e048d6448'
down_revision = 'd3fc17732622'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('company', 'address',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('company', 'logo',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.add_column('delivery', sa.Column('company_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('delivery', 'company_id')
    op.alter_column('company', 'logo',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('company', 'address',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###
