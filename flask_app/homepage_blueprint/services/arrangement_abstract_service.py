from abc import ABCMeta, abstractmethod


class ArrangementAbstractService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_arrangements(self):
        raise NotImplementedError()
