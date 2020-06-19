from abc import abstractmethod
from formaster.interactors.mixins.form_validation import FormValidationMixin
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import PresenterInterface
from formaster.exceptions.exceptions import *


class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int):
        self.storage = storage
        self.question_id = question_id
        self.form_id = form_id
        self.user_id = user_id

    def submit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            user_response_id = self.submit_form_response()
            return presenter.submit_form_response_return(user_response_id)
        except InvalidFormId:
            presenter.raise_invalid_form_id_exception()
        except FormClosed:
            presenter.raise_form_closed_exception()
        except QuestionDoesNotBelongToForm:
            presenter.raise_question_does_not_belong_to_form_exception()
        except InvalidUserResponseSubmit:
            presenter.raise_invalid_user_response_submitted()

    def submit_form_response(self):
        invalid_form_id = not self.storage.is_valid_form_id(self.form_id)
        if invalid_form_id:
            raise InvalidFormId
        self.validate_for_live_form(self.form_id)
        self.storage.validate_question_id_with_form(
            self.question_id, self.form_id)

        self._validate_user_response()
        user_response_id = self._create_user_response()

        return user_response_id

    @abstractmethod
    def _validate_user_response(self):
        pass

    @abstractmethod
    def _create_user_response(self) -> int:
        pass
