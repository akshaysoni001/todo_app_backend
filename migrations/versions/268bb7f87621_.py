"""empty message

Revision ID: 268bb7f87621
Revises: 191a629e33d4
Create Date: 2022-03-22 20:21:03.318316

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '268bb7f87621'
down_revision = '191a629e33d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todo_projects', 'due')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todo_projects', sa.Column('due', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
