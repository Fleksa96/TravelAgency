from abc import ABCMeta, abstractmethod


class ArrangementAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_arrangement_by_id(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_admin_id_from_arrangement_id(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements(self):
        raise NotImplementedError()

    @abstractmethod
    def search_all_arrangements(self, query_params):
        raise NotImplementedError()

    @abstractmethod
    def get_all_applications_for_travel_guide(self, travel_guide_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements_for_travel_guide(self, travel_guide_id):
        raise NotImplementedError()

    @abstractmethod
    def create_arrangement(self, new_arrangement):
        raise NotImplementedError()

    @abstractmethod
    def update_arrangement(self, arrangement, id):
        raise NotImplementedError()

    @abstractmethod
    def delete_arrangement(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_users_from_reservation(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_arrangement_by_destination_and_dates(self, new_arrangement):
        raise NotImplementedError()
