"""add auth fields to user

Revision ID: bac072e14542
Revises: dee5c657bf55
Create Date: 2026-07-24 02:33:50.875323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bac072e14542'
down_revision: Union[str, Sequence[str], None] = 'dee5c657bf55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
