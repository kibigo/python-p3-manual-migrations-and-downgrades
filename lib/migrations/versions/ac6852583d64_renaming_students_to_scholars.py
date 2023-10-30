"""Renaming students to scholars

Revision ID: ac6852583d64
Revises: 791279dd0760
Create Date: 2023-10-30 23:14:15.830360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac6852583d64'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='first_name')


def downgrade() -> None:
    op.alter_column('students', 'first_name', new_column_name='name')
