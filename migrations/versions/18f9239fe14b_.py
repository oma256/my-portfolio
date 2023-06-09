"""empty message

Revision ID: 18f9239fe14b
Revises: 2d14f796d2db
Create Date: 2023-03-28 20:12:07.951665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f9239fe14b'
down_revision = '2d14f796d2db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('position')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('position', sa.VARCHAR(length=128), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
