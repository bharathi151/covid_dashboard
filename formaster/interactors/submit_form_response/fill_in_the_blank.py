from formaster.interactors.submit_form_response.base import \
    BaseSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.exceptions.exceptions import *
from formaster.interactors.storages.dtos import UserFillInTheBlankResponseDTO

class FillInTheBlankQuestionSubmitFormResponseInteractor(
        BaseSubmitFormResponseInteractor):
    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_text: int):
        super().__init__(storage, question_id, form_id, user_id)
        self.user_submitted_text= user_submitted_text
    
    def _validate_user_response(self):
        pass

    def _create_user_response(self) -> int:
        user_response_dto = UserFillInTheBlankResponseDTO(
            self.user_id, self.question_id, self.user_submitted_text
        )
        response_id = self.storage.create_user_mcq_response(user_response_dto)
        return response_id
