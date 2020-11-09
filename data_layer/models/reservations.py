from flask_app import db
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint


class Reservation(db.Model):
    __tablename__ = 'reservation'
    __table_args__ = (
        UniqueConstraint('user_id',
                         'arrangement_id',
                         name='unique_u_r'
                         ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    arrangement_id = Column(
        Integer, ForeignKey('arrangement.id'), nullable=False
    )
