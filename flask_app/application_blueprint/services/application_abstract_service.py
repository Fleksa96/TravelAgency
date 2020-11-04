from abc import ABCMeta, abstractmethod


class ApplicatioAbstractService(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_all_arrangements_for_travel_guide(self, travel_guide_id):
        raise NotImplementedError()
