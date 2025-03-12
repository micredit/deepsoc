"""Remove completed_at from Task model

Revision ID: 4b689ba9b54b
Revises: e2fb2f8641e9
Create Date: 2025-03-01 12:22:50.901176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b689ba9b54b'
down_revision = 'e2fb2f8641e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_column('completed_at')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completed_at', sa.DATETIME(), nullable=True))

    # ### end Alembic commands ###
