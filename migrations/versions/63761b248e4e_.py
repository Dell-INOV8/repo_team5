"""empty message

Revision ID: 63761b248e4e
Revises: 
Create Date: 2018-10-12 13:27:02.600443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63761b248e4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('interest1', sa.String(length=32), nullable=True),
    sa.Column('interest2', sa.String(length=32), nullable=True),
    sa.Column('interest3', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_interest1'), 'users', ['interest1'], unique=True)
    op.create_index(op.f('ix_users_interest2'), 'users', ['interest2'], unique=True)
    op.create_index(op.f('ix_users_interest3'), 'users', ['interest3'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('post',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('challenges', sa.String(length=300), nullable=True),
    sa.Column('learned', sa.String(length=300), nullable=True),
    sa.Column('need_help', sa.String(length=300), nullable=True),
    sa.Column('in_progress', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('post_id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_interest3'), table_name='users')
    op.drop_index(op.f('ix_users_interest2'), table_name='users')
    op.drop_index(op.f('ix_users_interest1'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
