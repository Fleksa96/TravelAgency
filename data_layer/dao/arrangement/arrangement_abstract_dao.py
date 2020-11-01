from abc import ABCMeta, abstractmethod


class ArrangementAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_arrangement_by_id(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements(self):
        raise NotImplementedError()

    @abstractmethod
    def create_arrangement(self, new_arrangement):
        raise NotImplementedError()

    @abstractmethod
    def update_arrangement(self, arrangement):
        raise NotImplementedError()

    @abstractmethod
    def delete_arrangement(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_users_from_reservation(self, arrangement_id):
        raise NotImplementedError()
