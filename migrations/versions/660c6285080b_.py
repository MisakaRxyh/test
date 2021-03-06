"""empty message

Revision ID: 660c6285080b
Revises: 
Create Date: 2018-04-17 00:34:55.351830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660c6285080b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('position',
    sa.Column('positionId', sa.Integer(), nullable=False),
    sa.Column('positionName', sa.String(length=20), nullable=False),
    sa.Column('companyShortName', sa.String(length=20), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('salary', sa.String(length=20), nullable=False),
    sa.Column('education', sa.String(length=20), nullable=False),
    sa.Column('workYear', sa.String(length=20), nullable=False),
    sa.Column('createTime', sa.Date(), nullable=False),
    sa.Column('skillName', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('positionId')
    )
    op.create_table('skill',
    sa.Column('skillID', sa.Integer(), nullable=False),
    sa.Column('skillName', sa.String(length=20), nullable=False),
    sa.Column('skillNum', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('skillID')
    )
    op.create_table('statistics',
    sa.Column('statisticsID', sa.Integer(), nullable=False),
    sa.Column('skillName', sa.String(length=20), nullable=False),
    sa.Column('positionCount', sa.Integer(), nullable=False),
    sa.Column('firstCity', sa.String(length=20), nullable=False),
    sa.Column('secondCity', sa.String(length=20), nullable=False),
    sa.Column('thirdCity', sa.String(length=20), nullable=False),
    sa.Column('mainSalary', sa.String(length=20), nullable=False),
    sa.Column('mainEducation', sa.String(length=20), nullable=False),
    sa.Column('cityImgUrl', sa.String(length=20), nullable=False),
    sa.Column('salaryImgUrl', sa.String(length=20), nullable=False),
    sa.Column('educationImgUrl', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('statisticsID')
    )
    op.create_table('user',
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(length=20), nullable=False),
    sa.Column('userAccount', sa.String(length=20), nullable=False),
    sa.Column('userPwd', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('userID')
    )
    op.create_table('collect',
    sa.Column('collectID', sa.Integer(), nullable=False),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('statisticsID', sa.Integer(), nullable=False),
    sa.Column('collectDate', sa.Date(), nullable=False),
    sa.Column('queryName', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['statisticsID'], ['statistics.statisticsID'], ),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('collectID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('collect')
    op.drop_table('user')
    op.drop_table('statistics')
    op.drop_table('skill')
    op.drop_table('position')
    # ### end Alembic commands ###
