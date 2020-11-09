"""empty message

Revision ID: 035e123b6e10
Revises: cf883aee8e05
Create Date: 2020-11-09 09:39:49.613501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '035e123b6e10'
down_revision = 'cf883aee8e05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservations')
    # ### end Alembic commands ###