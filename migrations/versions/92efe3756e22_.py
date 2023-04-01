"""empty message

Revision ID: 92efe3756e22
Revises: 330b6de658e3
Create Date: 2023-04-01 20:31:59.771234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92efe3756e22'
down_revision = '330b6de658e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('experience',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position_name', sa.String(length=128), nullable=True),
    sa.Column('is_present', sa.Boolean(), nullable=True),
    sa.Column('date_begin', sa.Date(), nullable=True),
    sa.Column('date_end', sa.Date(), nullable=True),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experience_description',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('experience_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.ForeignKeyConstraint(['experience_id'], ['experience.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('resume',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('position_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['position_id'], ['position.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('education',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('degree', sa.String(length=128), nullable=True),
    sa.Column('major', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=512), nullable=True),
    sa.Column('date_begin', sa.Date(), nullable=True),
    sa.Column('date_end', sa.Date(), nullable=True),
    sa.Column('city', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['resume_id'], ['resume.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('intro', sa.String(length=512), nullable=True),
    sa.Column('city', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('phone', sa.String(length=128), nullable=True),
    sa.Column('resume_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['resume_id'], ['resume.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('summary')
    op.drop_table('education')
    op.drop_table('resume')
    op.drop_table('experience_description')
    op.drop_table('experience')
    # ### end Alembic commands ###