from abc import ABCMeta, abstractmethod


class ApplicationAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_application(self, application):
        raise NotImplementedError()
