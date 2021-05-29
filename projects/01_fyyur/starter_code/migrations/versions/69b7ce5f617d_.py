"""empty message

Revision ID: 69b7ce5f617d
Revises: 291a9b4b9b71
Create Date: 2021-05-03 10:28:06.602670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69b7ce5f617d'
down_revision = '291a9b4b9b71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=False))
    op.add_column('Show', sa.Column('start_time', sa.String(length=120), nullable=False))
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    op.drop_column('Show', 'name')
    op.drop_column('Show', 'city')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('city', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('Show', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'venue_id')
    op.drop_column('Show', 'start_time')
    op.drop_column('Show', 'artist_id')
    # ### end Alembic commands ###
