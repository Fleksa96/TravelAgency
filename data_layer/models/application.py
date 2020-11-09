from flask_app import db
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship


class Application(db.Model):
    __tablename__ = 'application'
    __table_args__ = (
        UniqueConstraint('user_id',
                         'arrangement_id',
                         name='unique_u_a'
                         ),
    )

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    arrangement_id = Column(
        Integer, ForeignKey('arrangement.id'), nullable=False
    )
    request_status = Column(Integer, nullable=True, default=3)

    arrangement = relationship(
        'Arrangement',
        foreign_keys=[arrangement_id],
        backref='applications'
    )

    user = relationship(
        'User',
        foreign_keys=[user_id],
        backref='applications'
    )

    def __init__(self,
                 user_id=None,
                 arrangement_id=None,
                 request_status=3
                 ):
        self.user_id = user_id
        self.arrangement_id = arrangement_id
        self.request_status = request_status
