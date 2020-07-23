from abc import ABC
from abc import abstractmethod
from  typing import List


from gyaan.interactors.presenters.dtos import *

class PresenterInterface(ABC):
    @abstractmethod
    def raise_invalid_domain_id_exception(self):
        pass

    @abstractmethod
    def raise_invalid_domain_member_exception(self):
        pass

    @abstractmethod
    def get_domain_details_response(self, domain_details_dto: DomainDetailsDto):
        pass

    @abstractmethod
    def raise_invalid_post_ids(self, error):
        pass

    @abstractmethod
    def get_posts_response(self, complete_posts_dto: CompletePostDetailsDto):
        pass

    @abstractmethod
    def get_domain_posts_response(self, posts_complete_details_dtos: CompletePostDetailsDto):
        pass

    @abstractmethod
    def raise_invalid_limit_exception(self, error):
        pass

    @abstractmethod
    def raise_invalid_offset_exception(self, error):
        pass

    @abstractmethod
    def get_domain_with_posts_response(
            self, domain_with_posts_dto: CompletePostDetailsDto):
        pass