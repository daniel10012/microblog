"""followers

Revision ID: 2971b3bef457
Revises: 45fa8c7d31aa
Create Date: 2019-12-14 01:06:50.539542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2971b3bef457'
down_revision = '45fa8c7d31aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###