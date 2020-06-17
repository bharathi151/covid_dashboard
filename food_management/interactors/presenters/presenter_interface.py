from abc import ABC
from abc import abstractmethod
from  typing import List
from common.dtos import UserAuthTokensDTO


from covid_dashboard.interactors.storages.dtos import *

class PresenterInterface(ABC):

    @abstractmethod
    def raise_invalid_meal_id_exception(self):
        pass
    @abstractmethod
    def raise_invalid_meal_items_exception(self, error):
        pass

    @abstractmethod
    def raise_duplicate_meal_items_exception(self, error):
        pass

    @abstractmethod
    def raise_negative_quantity_items_exception(self, error):
        pass

    @abstractmethod
    def raise_invalid_items_exception(self, error):
        pass