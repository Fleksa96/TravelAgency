from flask_app import db
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint


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
