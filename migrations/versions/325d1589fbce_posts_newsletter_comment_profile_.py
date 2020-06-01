"""posts,newsletter,comment,profile,category tables V1

Revision ID: 325d1589fbce
Revises: 6d14af2506de
Create Date: 2020-06-01 20:05:49.908664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '325d1589fbce'
down_revision = '6d14af2506de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('newsletter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_newsletter_email'), 'newsletter', ['email'], unique=True)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=300), nullable=True),
    sa.Column('image', sa.String(length=64), nullable=True),
    sa.Column('image_url', sa.String(length=120), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('bio', sa.String(length=1000), nullable=True),
    sa.Column('image', sa.String(length=64), nullable=True),
    sa.Column('image_url', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_profile_email'), 'profile', ['email'], unique=True)
    op.create_index(op.f('ix_profile_name'), 'profile', ['name'], unique=True)
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('comment', sa.Text(length=1000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_email'), 'comment', ['email'], unique=True)
    op.create_index(op.f('ix_comment_name'), 'comment', ['name'], unique=True)
    op.create_index(op.f('ix_comment_timestamp'), 'comment', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_timestamp'), table_name='comment')
    op.drop_index(op.f('ix_comment_name'), table_name='comment')
    op.drop_index(op.f('ix_comment_email'), table_name='comment')
    op.drop_table('comment')
    op.drop_index(op.f('ix_profile_name'), table_name='profile')
    op.drop_index(op.f('ix_profile_email'), table_name='profile')
    op.drop_table('profile')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_newsletter_email'), table_name='newsletter')
    op.drop_table('newsletter')
    op.drop_table('category')
    # ### end Alembic commands ###