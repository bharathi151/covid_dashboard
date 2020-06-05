from covid_dashboard.interactors.storages.user_storage_interface import StorageInterface
from covid_dashboard.interactors.presenters.presenter_interface import PresenterInterface
from covid_dashboard.models import User
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage

class LogInUserInteractor:
    def __init__(self, storage: StorageInterface,
                 oauth2_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage

    def log_in_user(self,user_name: str, password: str):
        is_valid_user_name = self.storage.validate_username(user_name=user_name)
        invalid_user_name = not is_valid_user_name

        if invalid_user_name:
            self.presenter.raise_invalid_username_exception()
            return

        is_valid_password = self.storage.validate_password(
            user_name=user_name, password=password
        )

        invalid_password = not is_valid_password
        if invalid_password:
            self.presenter.raise_invalid_password_exception()
            return

        user_id = self.storage.get_user_id(
            user_name=user_name, password=password
        )

        oauth_interactor = OAuthUserAuthTokensService(
            oauth2_storage = self.oauth2_storage
        )
        print("oauth interactor")
        storage_resonse = oauth_interactor.create_user_auth_tokens(
            user_id=user_id
        )
        print("oauth_response")
        response = self.presenter.get_log_in_user_response(
             tokens_dto=storage_resonse
        )
        print("success")
        return response
