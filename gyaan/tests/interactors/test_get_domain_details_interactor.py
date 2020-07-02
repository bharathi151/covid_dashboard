from unittest.mock import create_autospec, patch
import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

from gyaan.interactors.storages.dtos import *
from gyaan.interactors.presenters.dtos import *

from gyaan.interactors.domain_details_interactor import GetDomainDetailsInteractor
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface


def test_get_domain_details_when_invalid_domain_id_given_raise_invalid_domain_id_exception():
    #arrange
    domain_id=1
    user_id=1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_domain_id.return_value = False
    presenter.raise_invalid_domain_id_exception.side_effect = NotFound
    interactor = GetDomainDetailsInteractor(
        storage = storage
    )
    #act
    with pytest.raises(NotFound):
        interactor.get_domain_details_wrapper(
            presenter=presenter,
            domain_id=domain_id,
            user_id=user_id
        )
    #assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    presenter.raise_invalid_domain_id_exception.assert_called_once()


def test_get_domain_details_when_user_not_member_in_domain_given_raise_invalid_domain_member_exception():
    #arrange
    domain_id=1
    user_id=1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = False
    presenter.raise_invalid_domain_member_exception.side_effect = BadRequest
    interactor = GetDomainDetailsInteractor(
        storage = storage
    )
    #act
    with pytest.raises(BadRequest):
        interactor.get_domain_details_wrapper(
            presenter=presenter,
            domain_id=domain_id,
            user_id=user_id
        )
    #assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    presenter.raise_invalid_domain_member_exception.assert_called_once()


@patch(
        'gyaan.adapters.auth_service.AuthService.interface')
def test_get_domain_details_when_valid_details_given_where_user_is_domain_expert_return_domain_dto_with_requests_and_requested_users(
        interface, get_response, domain_dto, experts_dtos
    ):
    #arrange
    domain_id=1
    user_id=1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    expected_output = get_response
    domain_dto = domain_dto
    domain_stats_dto = DomainStatsDto(
        domain_id=1,
        posts_count=1,
        followers_count=3,
        bookmarks_count=3
    )
    experts_dtos = experts_dtos
    requests_dtos = [
        RequestDto(request_id=1,user_id=3),
        RequestDto(request_id=2,user_id=4)
    ]
    requested_user_dtos = [
        UserDto(name="user3", user_id=3, profile_pic="url3"),
        UserDto(name="user4", user_id=4, profile_pic="url4")
    ]
    is_user_domain_expert = True
    domain_details_dto = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=experts_dtos,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=requests_dtos,
            requested_users=requested_user_dtos
        )
    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = True
    storage.is_user_domain_expert.return_value = True
    storage.get_domain_dto.return_value = domain_dto
    storage.get_domain_experts_ids.return_value = [1, 2]
    # storage.get_domain_experts_dtos.return_value = experts_dtos
    storage.get_domain_stats_dto.return_value = domain_stats_dto
    storage.get_domain_join_requests.return_value = requests_dtos
    # storage.get_users_details_dtos.return_value = requested_user_dtos
    interface.get_user_dtos.side_effect = [experts_dtos, requested_user_dtos]
    presenter.get_domain_details_response.return_value = expected_output

    interactor = GetDomainDetailsInteractor(
        storage = storage
    )

    #act
    domain_details = interactor.get_domain_details_wrapper(
            presenter=presenter,
            domain_id=domain_id,
            user_id=user_id
        )

    #assert
    assert domain_details == expected_output
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    storage.get_domain_dto.assert_called_once_with(
        domain_id=domain_id
    )
    storage.get_domain_experts_ids.assert_called_once_with(
        domain_id=domain_id
    )
    # storage.get_domain_experts_dtos.assert_called_once_with(experts_ids=[1, 2])
    storage.get_domain_stats_dto.assert_called_once_with(domain_id=domain_id)
    # storage.get_users_details_dtos.assert_called_once_with(user_ids=[3, 4])
    presenter.get_domain_details_response.assert_called_once_with(domain_details_dto=domain_details_dto)


@patch(
        'gyaan.adapters.auth_service.AuthService.interface')
def test_get_domain_details_when_valid_details_given_where_user_is_not_domain_expert_return_domain_dto_with_empty_requests_and_requested_users(
        interface, get_response, domain_dto, experts_dtos
    ):
    #arrange
    domain_id=1
    user_id=1

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    expected_output = get_response
    domain_dto = domain_dto
    domain_stats_dto = DomainStatsDto(
        domain_id=1,
        posts_count=1,
        followers_count=3,
        bookmarks_count=3
    )
    experts_dtos = experts_dtos
    requests_dtos = []
    requested_user_dtos = []
    is_user_domain_expert = False
    domain_details_dto = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats_dto,
            domain_experts=experts_dtos,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            join_requests=requests_dtos,
            requested_users=requested_user_dtos
        )

    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = True
    storage.is_user_domain_expert.return_value = False
    storage.get_domain_dto.return_value = domain_dto
    storage.get_domain_experts_ids.return_value = [1, 2]
    # storage.get_domain_experts_dtos.return_value = experts_dtos
    storage.get_domain_stats_dto.return_value = domain_stats_dto
    storage.get_domain_join_requests.return_value = requests_dtos
    # storage.get_users_details_dtos.return_value = requested_user_dtos
    interface.get_user_dtos.side_effect = [experts_dtos, []]
    presenter.get_domain_details_response.return_value = expected_output

    interactor = GetDomainDetailsInteractor(
        storage = storage
    )

    #act
    domain_details = interactor.get_domain_details_wrapper(
            presenter=presenter,
            domain_id=domain_id,
            user_id=user_id
        )
    #assert
    assert domain_details == expected_output
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    storage.get_domain_dto.assert_called_once_with(
        domain_id=domain_id
    )
    storage.get_domain_experts_ids.assert_called_once_with(
        domain_id=domain_id
    )
    # storage.get_domain_experts_dtos.assert_called_once_with(experts_ids=[1, 2])
    storage.get_domain_stats_dto.assert_called_once_with(domain_id=domain_id)
    presenter.get_domain_details_response.assert_called_once_with(domain_details_dto=domain_details_dto)
