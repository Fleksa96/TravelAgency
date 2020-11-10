"""empty message

Revision ID: 653642bbe828
Revises: dbddacd0f384
Create Date: 2020-11-09 17:33:50.429199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653642bbe828'
down_revision = 'dbddacd0f384'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_u_r', 'implementation', ['user_id', 'arrangement_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_u_r', 'implementation', type_='unique')
    # ### end Alembic commands ###