from unittest.mock import create_autospec
import pytest
from formaster.interactors.storages.dtos import *
from formaster.exceptions.exceptions import *
from formaster.interactors.submit_form_response.mcq_question import MCQQuestionSubmitFormResponseInteractor
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.interactors.storages.storage_interface import StorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest


def test_mcq_question_when_question_not_in_form_questions_raise_question_does_not_belong_to_form_exception():
    #arrange
    question_id = 1
    form_id = 1
    user_id = 1
    user_submitted_option_id = 4
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_form_id.return_value = True
    storage.get_form_status.return_value = True
    storage.validate_question_id_with_form.return_value = True
    storage.get_option_ids_for_question.return_value = [1, 2, 3]
    presenter.raise_invalid_user_response_submitted.side_effect = BadRequest
    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage = storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        user_submitted_option_id=user_submitted_option_id
    )
    #act
    with pytest.raises(BadRequest):
        response = interactor.submit_form_response_wrapper(
            presenter=presenter
        )
    #assert
    storage.is_valid_form_id.assert_called_once_with(
        form_id=form_id
    )
    storage.get_form_status.assert_called_once_with(
        form_id=form_id
    )
    storage.validate_question_id_with_form.assert_called_once_with(
        question_id=question_id, form_id=form_id
    )
    storage.get_option_ids_for_question.assert_called_once_with(question_id=question_id)
    presenter.raise_invalid_user_response_submitted.assert_called_once()

def test_mcq_question_when_valid_details_given_return_response_id():
    #arrange
    question_id = 1
    form_id = 1
    user_id = 1
    user_submitted_option_id = 1
    response_id = 1
    expected_output = {"response_id": 1}
    user_response_dto = UserMCQResponseDTO(
        user_id=1,
        question_id=1,
        user_submitted_option_id=1
    )
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_form_id.return_value = True
    storage.get_form_status.return_value = True
    storage.validate_question_id_with_form.return_value = True
    storage.get_option_ids_for_question.return_value = [1, 2, 3]
    storage.create_user_mcq_response.return_value = response_id
    presenter.submit_form_response_return.return_value = expected_output
    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage = storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id,
        user_submitted_option_id=user_submitted_option_id
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
    storage.get_option_ids_for_question.assert_called_once_with(question_id=question_id)
    storage.create_user_mcq_response.assert_called_once_with(user_response_dto=user_response_dto)
    presenter.submit_form_response_return.assert_called_once()
