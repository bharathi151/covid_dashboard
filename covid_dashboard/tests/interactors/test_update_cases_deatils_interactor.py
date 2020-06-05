from unittest.mock import create_autospec
import pytest
import datetime
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.interactors.update_cases_details_interactor import UpdateCasesDetailsInteractor
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.interactors.storages.user_storage_interface import StorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_update_cases_given_valid_details_updates_cases():
    #arrange
    mandal_id=1,
    confirmed_cases=2,
    deaths=0,
    date=datetime.date(2020,5,30)
    recovered_cases=1
    mock_presenter_response = {
        "mandal_id": 1,
        "date": "30/05/2020",
        "total_confirmed_cases": 2,
        "total_recovered_cases": 1,
        "total_deaths":0
    }
    stats_dto = CasesDetailsDto(
        mandal_id=1,
        date="30/05/2020",
        total_confirmed_cases=2,
        total_recovered_cases=1,
        total_deaths=0
    )

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.update_cases_details.return_value = stats_dto
    storage.is_mandal_data_for_date_already_existed.return_value = True
    presenter.update_cases_details_response.return_value = mock_presenter_response
    interactor = UpdateCasesDetailsInteractor(
        storage = storage,
        presenter = presenter
    )
    #act
    response = interactor.update_cases_details(
        mandal_id=mandal_id,
        date=date,
        confirmed_cases=confirmed_cases,
        deaths=deaths,
        recovered_cases=recovered_cases)
    #assert
    storage.update_cases_details.assert_called_once_with(
        mandal_id=mandal_id,
        date=date,
        confirmed_cases=confirmed_cases,
        deaths=deaths,
        recovered_cases=recovered_cases
    )
    presenter.update_cases_details_response.assert_called_once_with(
        stats_dto=stats_dto
    )

    assert response == mock_presenter_response

def test_update_cases_given_invalid_mandal_id_raise_invalid_mandal_id_exception(
    create_districts,create_state):
    #arrange
    mandal_id=1,
    confirmed_cases=2,
    deaths=0,
    date=datetime.date(2020,5,30)
    recovered_cases=1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_mandal_id.return_value = False
    presenter.raise_invalid_mandal_id_exception.side_effect = NotFound
    interactor = UpdateCasesDetailsInteractor(
        storage = storage,
        presenter = presenter
    )
    #act
    with pytest.raises(NotFound):
         interactor.update_cases_details(
            mandal_id=mandal_id,
            date=date,
            confirmed_cases=confirmed_cases,
            deaths=deaths,
            recovered_cases=recovered_cases)
   
    #assert
    storage.is_valid_mandal_id.assert_called_once_with(
        mandal_id=mandal_id
    )
    presenter.raise_invalid_mandal_id_exception.assert_called_once()

def test_update_cases_given_existed_mandal_id_and_date_raise_data_already_existed_exception(
    create_districts,create_state):
    #arrange
    mandal_id=1,
    confirmed_cases=2,
    deaths=0,
    date=datetime.date(2020,5,30)
    recovered_cases=1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_mandal_id.return_value = True
    storage.is_mandal_data_for_date_already_existed.return_value = False
    presenter.raise_stats_not_existed.side_effect = NotFound
    interactor = UpdateCasesDetailsInteractor(
        storage = storage,
        presenter = presenter
    )
    #act
    with pytest.raises(NotFound):
         interactor.update_cases_details(
            mandal_id=mandal_id,
            date=date,
            confirmed_cases=confirmed_cases,
            deaths=deaths,
            recovered_cases=recovered_cases)
   
    #assert
    storage.is_mandal_data_for_date_already_existed.assert_called_once_with(
       date=date, mandal_id=mandal_id
    )
    presenter.raise_stats_not_existed.assert_called_once()



# def test_sign_in_interactor_with_inavalid_user_name_raise_inavlid_user_name_exception():
#     #arrange
#     user_name = "bharathi151273"
#     password = "rgukt123"
#     invalid_username = False
#     storage = create_autospec(StorageInterface)
#     presenter = create_autospec(PresenterInterface)
#     oauth2_storage = OAuth2SQLStorage
#     storage.validate_username.return_value = invalid_username
#     presenter.raise_invalid_username_exception.side_effect = NotFound

#     interactor = LogInUserInteractor(
#             storage=storage,
#             oauth2_storage=oauth2_storage,
#             presenter=presenter
#     )

#     with pytest.raises(NotFound):
#         interactor.log_in_user(
#             user_name=user_name, password = password
#         )
#     #assert
#     storage.validate_username.assert_called_once_with(
#         user_name=user_name
#     )
#     presenter.raise_invalid_username_exception.assert_called_once()