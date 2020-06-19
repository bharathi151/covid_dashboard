from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def get_create_post_response(self, post_id: int):
        pass

    @abstractmethod
    def raise_invalid_post_id_exception(self):
        pass

    @abstractmethod
    def get_create_comment_response(self, comment_id: int):
        pass

    @abstractmethod
    def raise_invalid_form_id_exception(self):
        pass

    @abstractmethod
    def raise_form_closed_exception(self):
        pass

    @abstractmethod
    def raise_question_does_not_belong_to_form_exception(self):
        pass

    @abstractmethod
    def raise_invalid_user_response_submitted(self):
        pass

    @abstractmethod
    def submit_form_response_return(self, response_id: int):
        pass