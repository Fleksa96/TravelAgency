from abc import ABCMeta, abstractmethod


class UserAbstractService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_new_tourist(self, new_user):
        raise NotImplementedError()

    @abstractmethod
    def login_user(self, user):
        raise NotImplementedError()

    @abstractmethod
    def get_all_travel_guides_without_arrangement(self, arrangement_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_travel_guides_with_application(self, arrangement_id):
        raise NotImplementedError()
