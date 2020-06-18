from typing import List
from gyaan.interactors.storages.storage_interface import StorageInterface
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.dtos import *
from gyaan.constants.exceptions import *

class GetDomainDetailsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_domain_details_wrapper(self, 
                           presenter: PresenterInterface,
                           domain_id: int,
                           user_id: int):
        self.presenter = presenter
        try:
           domain_details_dto = self.get_domain_details(
                domain_id=domain_id,
                user_id=user_id
            )
        except InvalidDomainId:
            return self.presenter.raise_invalid_domain_id_exception()
        except UserNotDomainFollower:
            return self.presenter.raise_invalid_domain_member_exception()

        return self.presenter.get_domain_details_response(
                domain_details_dto=domain_details_dto
            )

    def get_domain_details(self, domain_id: int, user_id: int):
        is_invalid_domain_id = not self.storage.is_valid_domain_id(domain_id=domain_id)
        if is_invalid_domain_id:
            raise InvalidDomainId

        is_user_not_domain_member = not self.storage.is_user_domain_follower(
            domain_id=domain_id, user_id=user_id
        )
        if is_user_not_domain_member:
            raise UserNotDomainFollower

        domain_dto = self.storage.get_domain_dto(domain_id=domain_id)
        experts_ids = self.storage.get_domain_experts_ids(domain_id=domain_id)
        experts_dtos = self.storage.get_domain_experts_dtos(experts_ids=experts_ids)
        domain_stats_dto = self.storage.get_domain_stats_dto(domain_id=domain_id)

        is_user_domain_expert = self.storage.is_user_domain_expert(
            domain_id=domain_id, user_id=user_id
        )
        join_requests, requested_user_dtos = [], []
        if is_user_domain_expert:
            join_requests, requested_user_dtos = self. \
                    _get_requests_details(domain_id=domain_id)
        domain_details_dto = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=experts_dtos,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=join_requests,
            requested_users=requested_user_dtos
        )
        return domain_details_dto

    def _get_requests_details(self, domain_id):
        domain_join_requests= self.storage.get_domain_join_requests(
            domain_id=domain_id
        )
        requested_user_ids = [dto.user_id for dto in domain_join_requests]
        requests_user_dtos = self.storage.get_users_details_dtos(
            user_ids=requested_user_ids
        )
        return domain_join_requests, requests_user_dtos

