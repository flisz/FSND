"""empty message

Revision ID: 06ed4a1caa86
Revises: 27f33d6079c0
Create Date: 2020-06-18 12:07:56.633887

"""
from alembic import op
from sqlalchemy.sql import table, column
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06ed4a1caa86'
down_revision = '27f33d6079c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('state', sa.String(length=2), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    #  Add cities from the other two tables
    op.execute(
        """
        INSERT INTO cities (name, state) (
        SELECT
        COALESCE(venues.city, artists.city) AS name,
        COALESCE(venues.state, artists.state) AS state
        FROM venues FULL OUTER JOIN artists
        ON (venues.state = artists.state)
        GROUP BY 1, 2 
        /* error is thrown unless columns are referenced by position */
        );
        """
    )
    # update artists table
    op.add_column('artists', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'artists', 'cities', ['city_id'], ['id'])
    op.execute(
        """
        UPDATE artists
        SET city_id = (
        SELECT cities.id FROM cities 
        WHERE artists.city = cities.name AND artists.state = cities.state
        );
        """
    )
    op.alter_column('artists', 'city_id', nullable=False)
    # update venues table
    op.add_column('venues', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'venues', 'cities', ['city_id'], ['id'])
    op.execute(
        """
        UPDATE venues
        SET city_id = (
        SELECT cities.id FROM cities 
        WHERE venues.city = cities.name AND venues.state = cities.state
        );
        """
    )
    op.alter_column('venues', 'city_id', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("venues_city_id_fkey", 'venues', type_='foreignkey')
    op.drop_column('venues', 'city_id')
    op.drop_constraint("artists_city_id_fkey", 'artists', type_='foreignkey')
    op.drop_column('artists', 'city_id')
    op.drop_table('cities')
    # ### end Alembic commands ###
