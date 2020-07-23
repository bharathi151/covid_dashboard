from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
import pytest
import datetime

from gyaan.interactors.storages.dtos import *
from gyaan.interactors.presenters.dtos import *
from gyaan.interactors.domain_posts_interactor import DomainPostsInteractor
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.presenters.presenter_interface import PresenterInterface
from gyaan.interactors.storages.storage_interface import StorageInterface


def test_get_domain_posts_when_invalid_domain_id_given_raise_invalid_domain_id_exception():
    #arrange
    domain_id = 1
    user_id = 1
    limit = 3
    offset = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_domain_id.return_value = False
    presenter.raise_invalid_domain_id_exception.side_effect = NotFound
    interactor = DomainPostsInteractor(
        storage = storage
    )
    #act
    with pytest.raises(NotFound):
        interactor.get_domain_posts_wrapper(
            presenter=presenter,
            user_id=user_id,
            domain_id=domain_id,
            limit=limit,
            offset=offset
        )
    #assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    presenter.raise_invalid_domain_id_exception.assert_called_once()

def test_get_domain_posts_when_user_not_member_in_domain_given_raise_invalid_domain_member_exception():
    #arrange
    domain_id = 1
    user_id = 1
    limit = 3
    offset = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = False
    presenter.raise_invalid_domain_member_exception.side_effect = BadRequest
    interactor = DomainPostsInteractor(
        storage = storage
    )
    #act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
            presenter=presenter,
            user_id=user_id,
            domain_id=domain_id,
            limit=limit,
            offset=offset
        )
    #assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    presenter.raise_invalid_domain_member_exception.assert_called_once()

def test_get_domain_posts_when_invalid_limit_given_raise_invalid_limit_exception():
    #arrange
    domain_id = 1
    user_id = 1
    limit = 0
    offset = 2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = True
    presenter.raise_invalid_limit_exception.side_effect = BadRequest
    interactor = DomainPostsInteractor(
        storage = storage
    )
    #act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
            presenter=presenter,
            user_id=user_id,
            domain_id=domain_id,
            limit=limit,
            offset=offset
        )
    #assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    presenter.raise_invalid_limit_exception.assert_called_once()
    call_args = presenter.raise_invalid_limit_exception.call_args
    call_obj = call_args.kwargs
    error_obj = call_obj["error"].invalid_limit
    assert error_obj == 0

def test_get_domain_posts_when_invalid_offset_given_raise_invalid_offset_exception():
    #arrange
    domain_id = 1
    user_id = 1
    limit = 2
    offset = -2

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = True
    presenter.raise_invalid_offset_exception.side_effect = BadRequest
    interactor = DomainPostsInteractor(
        storage = storage
    )

    #act
    with pytest.raises(BadRequest):
        interactor.get_domain_posts_wrapper(
            presenter=presenter,
            user_id=user_id,
            domain_id=domain_id,
            limit=limit,
            offset=offset
        )

    #assert
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    presenter.raise_invalid_offset_exception.assert_called_once()
    call_args = presenter.raise_invalid_offset_exception.call_args
    call_obj = call_args.kwargs
    error_obj = call_obj["error"].invalid_offset
    assert error_obj == -2

from gyaan.tests.interactors.conftest import *
complete_posts_dto = complete_posts_dto
@patch.object(GetPostsInteractor,'get_posts',return_value=complete_posts_dto)
def test_get_domain_posts_when_valid_details_given_return_domain_posts(GetPostsInteractor):
    #arrange
    domain_id = 1
    user_id = 1
    limit = 1
    offset = 0

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    storage.is_valid_domain_id.return_value = True
    storage.is_user_domain_follower.return_value = True
    storage.get_domain_post_ids.return_value = [1]
    presenter.get_domain_posts_response.return_value = get_response
    interactor = DomainPostsInteractor(
        storage = storage
    )
    #act
    response = interactor.get_domain_posts_wrapper(
            presenter=presenter,
            user_id=user_id,
            domain_id=domain_id,
            limit=limit,
            offset=offset
        )
    #assert
    assert response == get_response
    storage.is_valid_domain_id.assert_called_once_with(
        domain_id=domain_id
    )
    storage.is_user_domain_follower.assert_called_once_with(
        domain_id=domain_id, user_id=user_id
        )
    storage.get_domain_post_ids.assert_called_once_with(
        domain_id=domain_id, offset=offset, limit=limit
    )
    presenter.get_domain_posts_response.assert_called_once_with(posts_complete_details_dtos=complete_posts_dto)