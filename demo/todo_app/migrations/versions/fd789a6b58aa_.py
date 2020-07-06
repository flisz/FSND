"""empty message

Revision ID: fd789a6b58aa
Revises: 1010f0fd9c9f
Create Date: 2020-06-11 18:35:37.109721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd789a6b58aa'
down_revision = '1010f0fd9c9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_lists',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todo_lists', ['list_id'], ['id'])
    # ### end Alembic commands ###
    op.execute("""INSERT INTO todo_lists (name) VALUES ('Unassigned');""")
    op.execute('UPDATE todos SET list_id = 1 WHERE list_id IS NULL;')
    op.alter_column('todos', 'list_id', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('todos_list_id_fkey', 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todo_lists')
    # ### end Alembic commands ###