from flask_app import db
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint,\
    CheckConstraint, Float


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
    num_of_places = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    def __init__(self,
                 user_id,
                 arrangement_id,
                 num_of_places):
        self.user_id = user_id
        self.arrangement_id = arrangement_id
        self.num_of_places = num_of_places
