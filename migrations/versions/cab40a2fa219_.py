"""empty message

Revision ID: cab40a2fa219
Revises: 60df2c3bece5
Create Date: 2020-11-09 09:52:21.469117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cab40a2fa219'
down_revision = '60df2c3bece5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('implementation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'arrangement_id', name='unique_u_a')
    )
    op.drop_table('reservations')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('arrangement_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], name='reservations_arrangement_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='reservations_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reservations_pkey'),
    sa.UniqueConstraint('user_id', 'arrangement_id', name='unique_u_a')
    )
    op.drop_table('implementation')
    # ### end Alembic commands ###
