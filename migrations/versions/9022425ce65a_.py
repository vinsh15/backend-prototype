"""empty message

Revision ID: 9022425ce65a
Revises: 441f44aae45c
Create Date: 2021-02-05 21:11:42.297350

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9022425ce65a'
down_revision = '441f44aae45c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('phone', table_name='contact')
    op.drop_column('contact', 'gender')
    op.drop_column('contact', 'phone')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('phone', mysql.VARCHAR(length=40), nullable=False))
    op.add_column('contact', sa.Column('gender', mysql.VARCHAR(length=10), nullable=False))
    op.create_index('phone', 'contact', ['phone'], unique=True)
    # ### end Alembic commands ###