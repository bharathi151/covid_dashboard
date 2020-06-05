from covid_dashboard.interactors.storages.user_storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.models import User


class SignUpInteractor:
    def __init__(self, storage: StorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def sign_up(self,user_name: str, password: str, confirm_password: str):

        user_name, password= self.storage.sign_ip(
            user_name=user_name, password=password,
            confirm_password=confirm_password
        )

        response = self.presenter.get_sign_up_response(
             user_name=user_name,
             password=password
        )
        print("success")
        return response
