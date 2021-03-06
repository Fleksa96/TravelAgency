from abc import ABCMeta, abstractmethod


class ReservationAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_reservation(self,
                           user_id,
                           arrangement,
                           reservation):
        raise NotImplementedError()

    @abstractmethod
    def get_reservation_by_arrangement_user_id(self,
                                               user_id,
                                               arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def update_reservation(self,
                           arrangement,
                           reservation,
                           num_of_places):
        raise NotImplementedError()

    @abstractmethod
    def delete_reservations_for_arrangement(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_reservations_for_tourist(self, user_id):
        raise NotImplementedError()

    @abstractmethod
    def get_reservation_by_id(self, reservation_id):
        raise NotImplementedError()
