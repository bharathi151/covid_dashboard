from abc import ABC
from abc import abstractmethod
from typing import List
from formaster.interactors.storages.dtos import *

class StorageInterface(ABC):
    @abstractmethod
    def is_valid_form_id(self, form_id) -> bool:
        pass

    @abstractmethod
    def get_form_status(self, form_id) -> bool:
        pass

    @abstractmethod
    def validate_question_id_with_form(self, question_id, form_id) -> bool:
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id) -> List[int]:
        pass

    @abstractmethod
    def create_user_mcq_response(self, user_response_dto: UserMCQResponseDTO) -> int:
        pass