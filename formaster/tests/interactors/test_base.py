from unittest.mock import create_autospec
import pytest
from formaster.interactors.storages.dtos import *
from formaster.exceptions.exceptions import *
from formaster.interactors.submit_form_response.base import BaseSubmitFormResponseInteractor
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.interactors.storages.storage_interface import StorageInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest

def test_base_when_invalid_form_id_given_raise_invalid_form_id_exception():
    #arrange
    question_id = 1
    form_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_form_id.return_value = False
    presenter.raise_invalid_form_id_exception.side_effect = NotFound
    interactor = BaseSubmitFormResponseInteractor(
        storage = storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id
    )
    #act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(
            presenter=presenter
        )
    #assert
    storage.is_valid_form_id.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_invalid_form_id_exception.assert_called_once()

def test_base_when_form_is_closed_given_raise_form_closed_exception():
    #arrange
    question_id = 1
    form_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_form_id.return_value = True
    storage.get_form_status.return_value = False
    presenter.raise_form_closed_exception.side_effect = BadRequest
    interactor = BaseSubmitFormResponseInteractor(
        storage = storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id
    )
    #act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(
            presenter=presenter
        )
    #assert
    storage.is_valid_form_id.assert_called_once_with(
        form_id=form_id
    )
    storage.get_form_status.assert_called_once_with(
        form_id=form_id
    )
    presenter.raise_form_closed_exception.assert_called_once()

def test_base_when_question_not_in_form_questions_raise_question_does_not_belong_to_form_exception():
    #arrange
    question_id = 1
    form_id = 1
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    storage.is_valid_form_id.return_value = True
    storage.get_form_status.return_value = True
    storage.validate_question_id_with_form.side_effect = QuestionDoesNotBelongToForm
    presenter.raise_question_does_not_belong_to_form_exception.side_effect = BadRequest
    interactor = BaseSubmitFormResponseInteractor(
        storage = storage,
        question_id=question_id,
        form_id=form_id,
        user_id=user_id
    )
    #act
    with pytest.raises(BadRequest):
        interactor.submit_form_response_wrapper(
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
    presenter.raise_question_does_not_belong_to_form_exception.assert_called_once()