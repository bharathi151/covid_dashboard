from unittest.mock import create_autospec
import pytest
from formaster.interactors.storages.dtos import *
from formaster.exceptions.exceptions import *
from formaster.interactors.submit_form_response.fill_in_the_blank import FillInTheBlankQuestionSubmitFormResponseInteractor
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.interactors.storages.storage_interface import StorageInterface


def test_fill_in_the_blank_question_when_valid_details_given_return_response_id():
    #arrange
    question_id = 1
    form_id = 1
    user_id = 1
    user_submitted_text = "world"
    response_id = 1
    expected_output = {"response_id": 1}
    user_response_dto = UserFillInTheBlankResponseDTO(
        user_id=1,
        question_id=1,
        user_submitted_text="world"
    )
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_form_id.return_value = True
    storage.get_form_status.return_value = True
    storage.validate_question_id_with_form.return_value = True
    storage.create_user_mcq_response.return_value = response_id
    presenter.submit_form_response_return.return_value = expected_output
    interactor = FillInTheBlankQuestionSubmitFormResponseInteractor(
        storage = storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        user_submitted_text=user_submitted_text
    )
    #act
    response = interactor.submit_form_response_wrapper(
            presenter=presenter
        )
    #assert
    assert response == expected_output
    storage.is_valid_form_id.assert_called_once_with(
        form_id=form_id
    )
    storage.get_form_status.assert_called_once_with(
        form_id=form_id
    )
    storage.validate_question_id_with_form.assert_called_once_with(
        question_id=question_id, form_id=form_id
    )
    storage.create_user_mcq_response.assert_called_once_with(user_response_dto=user_response_dto)
    presenter.submit_form_response_return.assert_called_once()
