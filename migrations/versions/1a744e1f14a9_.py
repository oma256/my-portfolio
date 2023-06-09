"""empty message

Revision ID: 1a744e1f14a9
Revises: f496721928d8
Create Date: 2023-04-01 19:12:10.926127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a744e1f14a9'
down_revision = 'f496721928d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('position', schema=None) as batch_op:
        batch_op.add_column(sa.Column('freelance', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('position', schema=None) as batch_op:
        batch_op.drop_column('freelance')

    # ### end Alembic commands ###
