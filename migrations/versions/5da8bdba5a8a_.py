"""empty message

Revision ID: 5da8bdba5a8a
Revises: 
Create Date: 2021-01-25 00:55:36.460717

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5da8bdba5a8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotes',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('open', sa.Numeric(), nullable=True),
    sa.Column('high', sa.Numeric(), nullable=True),
    sa.Column('low', sa.Numeric(), nullable=True),
    sa.Column('close', sa.Numeric(), nullable=True),
    sa.Column('adj_close', sa.Numeric(), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('wvolume', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotes')
    # ### end Alembic commands ###
