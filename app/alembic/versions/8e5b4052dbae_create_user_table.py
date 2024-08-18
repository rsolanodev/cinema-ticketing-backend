"""Create User table

Revision ID: 8e5b4052dbae
Revises:
Create Date: 2024-08-17 23:28:18.362473

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '8e5b4052dbae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usermodel',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('full_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('hashed_password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usermodel_email'), 'usermodel', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usermodel_email'), table_name='usermodel')
    op.drop_table('usermodel')
    # ### end Alembic commands ###
