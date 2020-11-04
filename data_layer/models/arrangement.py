from sqlalchemy import (Column,
                        Integer,
                        String,
                        Date,
                        Float,
                        ForeignKey)

from flask_app import db
from sqlalchemy.orm import relationship


guides_applications = db.Table('applications',
                               Column('id', Integer, primary_key=True),
                               Column('user_id', Integer,
                                      ForeignKey('user.id')),
                               Column('arrangement_id', Integer,
                                      ForeignKey('arrangement.id',
                                                 ondelete='CASCADE')),
                               Column('request_status', Integer,
                                      default=1)
                               )


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
    users_applications = relationship(
        "User",
        secondary=guides_applications,
        backref="guides_applications")

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
