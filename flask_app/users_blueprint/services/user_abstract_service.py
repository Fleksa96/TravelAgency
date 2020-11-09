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
    def get_user_by_id(self, user_id):
        raise NotImplementedError()

    @abstractmethod
    def update_user(self, user_id, data):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements_for_guide(self, travel_guide_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_applications_for_guide(self, travel_guide_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_arrangements_for_tourist(self, tourist_id):
        raise NotImplementedError()
