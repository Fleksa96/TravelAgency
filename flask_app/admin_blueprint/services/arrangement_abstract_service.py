from abc import ABCMeta, abstractmethod


class ArrangementAbstractService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_arrangement(self, data):
        raise NotImplementedError()
