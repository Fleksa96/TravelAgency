from abc import ABCMeta, abstractmethod


class ArrangementAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_arrangements(self):
        raise NotImplementedError()

    @abstractmethod
    def create_arrangement(self, data):
        raise NotImplementedError()

    @abstractmethod
    def delete_arrangement(self, data):
        raise NotImplementedError()

    @abstractmethod
    def send_email_of_cancellation(self, data):
        raise NotImplementedError()
