from abc import ABCMeta, abstractmethod


class UserAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_user(self, new_user):
        raise NotImplementedError()

    @abstractmethod
    def check_identity(self, data):
        raise NotImplementedError()

    @abstractmethod
    def get_user_by_username(self, username):
        raise NotImplementedError()

    @abstractmethod
    def get_user_by_id(self, user_id):
        raise NotImplementedError()

    @abstractmethod
    def get_all_travel_guides_with_spare_time(self, arrangement):
        raise NotImplementedError()

    @abstractmethod
    def get_all_travel_guides_with_application(self, arrangement):
        raise NotImplementedError()

    @abstractmethod
    def get_all_travel_guides_without_any_arrangement(self):
        raise NotImplementedError()

    def get_user_by_email(self, email):
        raise NotImplementedError()
