"""empty message

Revision ID: 45e13d581215
Revises: df9af7564ebd
Create Date: 2020-06-16 21:59:52.579266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e13d581215'
down_revision = 'df9af7564ebd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('artists', sa.Column('website', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('venues', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    op.add_column('venues', sa.Column('website', sa.String(), nullable=True))
    # ### end Alembic commands ###

    #  Demo data for Venues
    op.execute(
        """
        INSERT INTO venues
        (name, genres, address, city, state, phone, website, facebook_link, seeking_talent, seeking_description, image_link)
        VALUES (
        'The Musical Hop',
        'Jazz,Reggae,Swing,Classical,Folk',
        '1015 Folsom Street',
        'San Francisco',
        'CA',
        '123-123-1234',
        'https://www.themusicalhop.com',
        'https://www.facebook.com/TheMusicalHop',
        True,
        'We are on the lookout for a local artist to play every two weeks. Please call us.',
        'https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60'
        );
        """
    )

    op.execute(
        """
        INSERT INTO venues
        (name, genres, address, city, state, phone, website, facebook_link, seeking_talent, image_link)
        VALUES (
        'The Dueling Pianos Bar',
        'Classical,R&B,Hip-Hop',
        '335 Delancey Street',
        'New York',
        'NY',
        '914-003-1132',
        'https://www.theduelingpianos.com',
        'https://www.facebook.com/theduelingpianos',
        False,
        'https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80'
        );
        """
    )

    op.execute(
        """
        INSERT INTO venues
        (name, genres, address, city, state, phone, website, facebook_link, seeking_talent, image_link)
        VALUES (
        'Park Square Live Music & Coffee',
        'Rock n Roll,Jazz,Classical,Folk',
        '34 Whiskey Moore Ave',
        'San Francisco',
        'CA',
        '415-000-1234',
        'https://www.parksquarelivemusicandcoffee.com',
        'https://www.facebook.com/ParkSquareLiveMusicAndCoffee',
        False,
        'https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80'
        );
        """
    )

    # Artists Demo Data
    op.execute(
        """
        INSERT INTO artists
        (name, genres, city, state, phone, website, facebook_link, seeking_venue, seeking_description, image_link)
        VALUES (
        'Guns N Petals',
        'Rock n Roll',
        'San Francisco',
        'CA',
        '326-123-5000',
        'https://www.gunsnpetalsband.com',
        'https://www.facebook.com/GunsNPetals',
        True,
        'Looking for shows to perform at in the San Francisco Bay Area!',
        'https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80'
        );
        """
    )

    op.execute(
        """
        INSERT INTO artists
        (name, genres, city, state, phone, facebook_link, seeking_venue, image_link)
        VALUES (
        'Matt Quevedo',
        'Jazz',
        'New York',
        'NY',
        '300-400-5000',
        'https://www.facebook.com/mattquevedo923251523',
        False,
        'https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80'
        );        
        """
    )

    op.execute(
        """
        INSERT INTO artists
        (name, genres, city, state, phone, seeking_venue, image_link)
        VALUES (
        'The Wild Sax Band',
        'Jazz,Classical',
        'San Francisco',
        'CA',
        '432-325-5432',
        False,
        'https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80'
        );
        """
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venues', 'website')
    op.drop_column('venues', 'seeking_talent')
    op.drop_column('venues', 'seeking_description')
    op.drop_column('venues', 'genres')
    op.drop_column('artists', 'website')
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('artists', 'seeking_description')
    # ### end Alembic commands ###
    op.execute("""DELETE FROM artists;""")
    op.execute("""DELETE FROM venues;""")