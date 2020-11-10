"""empty message

Revision ID: 833091570806
Revises: cab40a2fa219
Create Date: 2020-11-09 09:56:17.608856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '833091570806'
down_revision = 'cab40a2fa219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_u_r', 'implementation', ['user_id', 'arrangement_id'])
    op.drop_constraint('unique_u_a', 'implementation', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_u_a', 'implementation', ['user_id', 'arrangement_id'])
    op.drop_constraint('unique_u_r', 'implementation', type_='unique')
    # ### end Alembic commands ###
