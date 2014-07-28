"""empty message

Revision ID: 3cb99a2244f6
Revises: 201fb4631987
Create Date: 2014-07-28 22:09:25.206718

"""

# revision identifiers, used by Alembic.
revision = '3cb99a2244f6'
down_revision = '201fb4631987'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.create_table('pvdata',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.Text(), nullable=False),
                    sa.Column('ac_1_u', sa.Integer(), nullable=True),
                    sa.Column('ac_1_i', sa.Float(), nullable=True),
                    sa.Column('dc_1_u', sa.Integer(), nullable=True),
                    sa.Column('dc_1_p', sa.Integer(), nullable=True),
                    sa.Column('ac_2_u', sa.Integer(), nullable=True),
                    sa.Column('ac_2_i', sa.Float(), nullable=True),
                    sa.Column('dc_2_u', sa.Integer(), nullable=True),
                    sa.Column('dc_2_p', sa.Integer(), nullable=True),
                    sa.Column('ac_3_u', sa.Integer(), nullable=True),
                    sa.Column('ac_3_i', sa.Float(), nullable=True),
                    sa.Column('dc_3_u', sa.Integer(), nullable=True),
                    sa.Column('dc_3_p', sa.Integer(), nullable=True),
                    sa.Column('current_power', sa.Integer(), nullable=True),
                    sa.Column('daily_energy', sa.Float(), nullable=True),
                    sa.Column('total_energy', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pv_data')
    ### end Alembic commands ###


def downgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.create_table('pv_data',
                    sa.Column('id', sa.INTEGER(), nullable=False),
                    sa.Column('created_at', sa.TEXT(), nullable=False),
                    sa.Column('ac_1_u', sa.INTEGER(), nullable=True),
                    sa.Column('ac_1_i', sa.FLOAT(), nullable=True),
                    sa.Column('dc_1_u', sa.INTEGER(), nullable=True),
                    sa.Column('dc_1_p', sa.INTEGER(), nullable=True),
                    sa.Column('ac_2_u', sa.INTEGER(), nullable=True),
                    sa.Column('ac_2_i', sa.FLOAT(), nullable=True),
                    sa.Column('dc_2_u', sa.INTEGER(), nullable=True),
                    sa.Column('dc_2_p', sa.INTEGER(), nullable=True),
                    sa.Column('ac_3_u', sa.INTEGER(), nullable=True),
                    sa.Column('ac_3_i', sa.FLOAT(), nullable=True),
                    sa.Column('dc_3_u', sa.INTEGER(), nullable=True),
                    sa.Column('dc_3_p', sa.INTEGER(), nullable=True),
                    sa.Column('current_power', sa.INTEGER(), nullable=True),
                    sa.Column('daily_energy', sa.FLOAT(), nullable=True),
                    sa.Column('total_energy', sa.INTEGER(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pvdata')
    ### end Alembic commands ###
