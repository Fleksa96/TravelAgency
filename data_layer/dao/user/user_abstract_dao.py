from abc import ABCMeta, abstractmethod


class UserAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_user(self, user):
        raise NotImplementedError()

    @abstractmethod
    def check_identity(self, data):
        raise NotImplementedError()
