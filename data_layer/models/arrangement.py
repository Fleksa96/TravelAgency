from sqlalchemy import (Column,
                        Integer,
                        String,
                        Date,
                        Float,
                        ForeignKey,
                        Boolean,
                        UniqueConstraint)

from flask_app import db
from sqlalchemy.orm import relationship


class Arrangement(db.Model):
    __tablename__ = 'arrangement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    description = Column(String(500), nullable=True)
    destination = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    free_places = Column(Integer, nullable=False)
    admin_id = Column(Integer, ForeignKey('user.id'))
    travel_guide_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    is_active = Column(Boolean, nullable=True, default=True)

    admin = relationship(
        'User',
        foreign_keys=[admin_id],
        backref='admin_arrangements'
    )

    travel_guide = relationship(
        'User',
        foreign_keys=[travel_guide_id],
        backref='tour_arrangements'
    )

    def __init__(self,
                 id=None,
                 start_date=None,
                 end_date=None,
                 description=None,
                 destination=None,
                 price=None,
                 free_places=None,
                 admin_id=None,
                 travel_guide_id=None
                 ):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.destination = destination
        self.price = price
        self.free_places = free_places
        self.admin_id = admin_id
        self.travel_guide_id = travel_guide_id
