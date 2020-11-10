"""empty message

Revision ID: dbddacd0f384
Revises: 833091570806
Create Date: 2020-11-09 17:31:40.307796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbddacd0f384'
down_revision = '833091570806'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.Column('request_status', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'arrangement_id', name='unique_u_a')
    )
    op.create_table('implementation',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('arrangement_id', sa.Integer(), nullable=False),
    sa.Column('num_of_places', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('reservation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('arrangement_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['arrangement_id'], ['arrangement.id'], name='reservation_arrangement_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='reservation_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='reservation_pkey'),
    sa.UniqueConstraint('user_id', 'arrangement_id', name='unique_u_r')
    )
    op.drop_table('implementation')
    op.drop_table('application')
    # ### end Alembic commands ###