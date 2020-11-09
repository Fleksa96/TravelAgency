from abc import ABCMeta, abstractmethod


class ArrangementAbstractService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_arrangement(self, data):
        raise NotImplementedError()

    @abstractmethod
    def update_arrangement(self, id, data):
        raise NotImplementedError()

    @abstractmethod
    def delete_arrangement(self, data):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements(self):
        raise NotImplementedError()

    @abstractmethod
    def get_arrangement_by_id(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements_depending_guide(self, has_travel_guide):
        raise NotImplementedError()

    @abstractmethod
    def create_application(self, travel_guide_id, post_data):
        raise NotImplementedError()

    @abstractmethod
    def get_all_guides_with_application(self, arrangement_id):
        raise NotImplementedError()
