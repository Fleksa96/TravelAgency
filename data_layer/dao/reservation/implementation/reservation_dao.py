from data_layer.dao.reservation.reservation_abstract_dao import \
    ReservationAbstractDao
from data_layer.models.arrangement import Arrangement
from data_layer.models.reservations import Reservation

from flask_app import db


class ReservationDao(ReservationAbstractDao):

    def create_reservation(self,
                           user_id,
                           arrangement,
                           reservation):
        arrangement.free_places -= reservation.num_of_places

        if reservation.num_of_places > 3:
            price = 3 * arrangement.price + \
                    (reservation.num_of_places - 3) * arrangement.price * 0.8
        else:
            price = reservation.num_of_places * arrangement.price

        reservation.price = price
        db.session.add(reservation)
        db.session.commit()

        return {"message": "You successfully created a reservation, "
                           'price of reservation is(eur): ' + str(price)}, 200

    def get_all_reservations_for_tourist(self, user_id):
        reservations = db.session.query(Reservation). \
            join(Arrangement, Arrangement.id == Reservation.arrangement_id).\
            filter(Arrangement.is_active.is_(True)).\
            filter(Reservation.user_id == user_id). \
            all()
        return reservations

    def get_reservation_by_arrangement_user_id(self,
                                               user_id,
                                               arrangement_id):
        reservation = db.session.query(Reservation). \
            filter(Reservation.arrangement_id == arrangement_id). \
            filter(Reservation.user_id == user_id). \
            first()
        return reservation

    def get_reservation_by_id(self, reservation_id):
        reservation = db.session.query(Reservation). \
            filter(Reservation.id == reservation_id). \
            first()
        return reservation

    def update_reservation(self,
                           arrangement,
                           reservation,
                           num_of_places):
        arrangement.free_places -= num_of_places
        reservation.num_of_places += num_of_places

        if reservation.num_of_places > 3:
            price = 3 * arrangement.price + \
                    (reservation.num_of_places - 3) * arrangement.price * 0.8
        else:
            price = reservation.num_of_places * arrangement.price

        reservation.price = price
        db.session.commit()

        return {"message": "You successfully updated a reservation, "
                           'price of reservation is(eur): ' + str(price)}, 200

    def delete_reservations_for_arrangement(self, arrangement_id):
        db.session.query(Reservation).\
            filter(Reservation.arrangement_id == arrangement_id).\
            delete()
        db.session.commit()
