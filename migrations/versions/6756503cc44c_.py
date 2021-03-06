"""empty message

Revision ID: 6756503cc44c
Revises: e6ac3c0e127e
Create Date: 2020-10-27 17:06:25.962444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6756503cc44c'
down_revision = 'e6ac3c0e127e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'user_type',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'user_type',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
