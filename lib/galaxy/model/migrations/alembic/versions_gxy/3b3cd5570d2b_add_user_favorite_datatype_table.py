"""Add user_favorite_datatype table

Revision ID: 3b3cd5570d2b
Revises: c44ae5f3dcf1
Create Date: 2025-06-24 13:39:39.253648

"""
import sqlalchemy as sa

from galaxy.model.migrations.util import (
    create_table,
    drop_table,
)

# revision identifiers, used by Alembic.
revision = '3b3cd5570d2b'
down_revision = 'c44ae5f3dcf1'
branch_labels = None
depends_on = None

TABLE_NAME = "user_favorite_datatype"

def upgrade():
    create_table(TABLE_NAME,
                 sa.Column("id", sa.Integer, primary_key=True),
                 sa.Column("user_id", sa.Integer, sa.ForeignKey("galaxy_user.id")),
                 sa.Column("datatype", sa.String(255)))


def downgrade():
    drop_table(TABLE_NAME)
