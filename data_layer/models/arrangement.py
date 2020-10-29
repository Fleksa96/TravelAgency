from sqlalchemy import (Column,
                        Integer,
                        String,
                        Date,
                        Float,
                        ForeignKey)
from flask_app import db
from sqlalchemy.orm import relationship


class Arrangement(db.Model):
    __tablename__='arrangement'

    id = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    description = Column(String(500), nullable=True)
    destination = Column(String(256), nullable=False)
    price = Column(Float, nullable=False)
    free_places = Column(Integer, nullable=False)
    admin_id = Column(Integer, ForeignKey('user.id'))
    tourist_guide_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    admin = relationship(
        'User',
        foreign_keys=[admin_id],
        backref='arrangements'
    )

    tourist_guide = relationship(
        'User',
        foreign_keys=[tourist_guide_id],
        backref='tour_arrangements'
    )
