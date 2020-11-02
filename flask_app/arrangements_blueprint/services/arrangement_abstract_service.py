from abc import ABCMeta, abstractmethod


class ArrangementAbstractService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_arrangement(self, data):
        raise NotImplementedError()

    @abstractmethod
    def update_arrangement(self, data):
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
    def get_all_arrangements_without_guide(self):
        raise NotImplementedError()
