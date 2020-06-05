from unittest.mock import create_autospec
import pytest
import datetime
from unittest.mock import patch
from covid_dashboard.interactors.sign_in_interactor import LogInUserInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.user_storage_interface import StorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token='VREaZ6F5XhqHk3TomMaGcML4MH14VI',
        refresh_token='YuGl5rueIghdXh0x8QLFWTz13C8kre',
        expires_in=datetime.datetime(2052, 2, 3, 12, 52, 0, 670849)
    )

@patch.object(OAuthUserAuthTokensService,'create_user_auth_tokens',return_value=token_dto)
def test_sign_in_interactor_with_valid_details_returns_user_oauth_tokens_object(
    OAuthUserAuthTokensService
    ):
    #arrange
    user_name = 1
    password = "rgukt123"
    user_id = 1
    mock_presenter_response = {"user_name": 1,
                               "access_token": 'VREaZ6F5XhqHk3TomMaGcML4MH14VI',
                               "refresh_token": 'YuGl5rueIghdXh0x8QLFWTz13C8kre',
                               "expires_in": datetime.datetime(
                                   2052, 2, 3, 12, 52, 0, 670849)
    }
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = OAuth2SQLStorage
    storage.get_user_id.return_value = user_id
    storage.validate_password.return_value = True
    storage.validate_username.return_value = True
    presenter.get_log_in_user_response.return_value = mock_presenter_response

    interactor = LogInUserInteractor(
        storage=storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )
    #act
    response = interactor.log_in_user(
        user_name=user_name, password = password
    )
    #assert
    storage.validate_username.assert_called_once_with(user_name=user_name)
    storage.validate_password.assert_called_once_with(
        user_name=user_name, password=password
    )
    storage.get_user_id.assert_called_once_with(
        user_name=user_name, password=password
    )
    presenter.get_log_in_user_response.assert_called_once_with(
        tokens_dto=token_dto
    )
    assert response == mock_presenter_response


def test_sign_in_interactor_with_inavalid_user_name_raise_inavlid_user_name_exception():
    #arrange
    user_name = "bharathi151273"
    password = "rgukt123"
    invalid_username = False
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = OAuth2SQLStorage
    storage.validate_username.return_value = invalid_username
    presenter.raise_invalid_username_exception.side_effect = NotFound

    interactor = LogInUserInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage,
            presenter=presenter
    )

    with pytest.raises(NotFound):
        interactor.log_in_user(
            user_name=user_name, password = password
        )
    #assert
    storage.validate_username.assert_called_once_with(
        user_name=user_name
    )
    presenter.raise_invalid_username_exception.assert_called_once()

def test_sign_in_interactor_with_inavalid_password_raise_inavlid_password_exception():
    #arrange
    user_name = "bharathi151273"
    password = "rgukt123"
    valid_username = True
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = OAuth2SQLStorage
    storage.validate_username.return_value = True
    storage.validate_password.return_value = False
    presenter.raise_invalid_password_exception.side_effect = BadRequest

    interactor = LogInUserInteractor(
            storage=storage,
            oauth2_storage=oauth2_storage,
            presenter=presenter
    )

    with pytest.raises(BadRequest):
        interactor.log_in_user(
            user_name=user_name, password = password
        )
    #assert
    storage.validate_username.assert_called_once_with(
        user_name=user_name
    )
    storage.validate_password.assert_called_once_with(
        user_name=user_name, password=password
    )
    presenter.raise_invalid_password_exception.assert_called_once()
