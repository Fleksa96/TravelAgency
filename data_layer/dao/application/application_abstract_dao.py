from abc import ABCMeta, abstractmethod


class ApplicationAbstractDao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_application(self, application):
        raise NotImplementedError()

    @abstractmethod
    def update_application_status(self, application, arrangement_id, user_id):
        raise NotImplementedError()

    @abstractmethod
    def get_application_by_arrangement_user_id(self, user_id, arrangement_id):
        raise NotImplementedError()
