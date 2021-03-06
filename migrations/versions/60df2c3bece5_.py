"""empty message

Revision ID: 60df2c3bece5
Revises: 035e123b6e10
Create Date: 2020-11-09 09:50:31.418347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '60df2c3bece5'
down_revision = '035e123b6e10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique1', 'reservations', ['user_id', 'arrangement_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_u_a', 'reservations', type_='unique')
    # ### end Alembic commands ###
