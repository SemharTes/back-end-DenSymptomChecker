"""adds admin model

Revision ID: 8d0965dd3d25
Revises: 
Create Date: 2023-02-01 17:46:37.818078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d0965dd3d25'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('admin_name', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('symptom',
    sa.Column('symptom_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('description_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('symptom_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('symptom')
    op.drop_table('admin')
    # ### end Alembic commands ###