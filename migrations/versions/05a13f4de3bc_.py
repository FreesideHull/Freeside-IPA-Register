"""empty message

Revision ID: 05a13f4de3bc
Revises: 
Create Date: 2018-06-09 04:52:02.516977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "05a13f4de3bc"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=120), nullable=False),
        sa.Column("uuid", sa.String(length=120), nullable=True),
        sa.Column("account_created", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("uuid"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###
