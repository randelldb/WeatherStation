"""empty message

Revision ID: 2ee4341e96db
Revises: 48a9f4b3cd00
Create Date: 2023-01-25 22:34:07.935641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ee4341e96db'
down_revision = '48a9f4b3cd00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sensors', schema=None) as batch_op:
        batch_op.add_column(sa.Column('displayed', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sensors', schema=None) as batch_op:
        batch_op.drop_column('displayed')

    # ### end Alembic commands ###
