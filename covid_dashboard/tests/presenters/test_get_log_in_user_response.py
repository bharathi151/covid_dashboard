import datetime
from unittest.mock import patch
from common.dtos import UserAuthTokensDTO
from covid_dashboard.presenters.presenter_implementation import PresenterImplementation
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

token_dto = UserAuthTokensDTO(
        user_id=1,
        access_token='VREaZ6F5XhqHk3TomMaGcML4MH14VI',
        refresh_token='YuGl5rueIghdXh0x8QLFWTz13C8kre',
        expires_in=datetime.datetime(2052, 2, 3, 12, 52, 0, 670849)
    )

@patch.object(OAuthUserAuthTokensService,'create_user_auth_tokens',return_value=token_dto)
def test_get_response_for_log_in_user_given_post_id_returns_tokens_dict(OAuthUserAuthTokensService):

    expected_tokens_dict = {"user_id": 1,
                            "access_token": 'VREaZ6F5XhqHk3TomMaGcML4MH14VI',
                            "refresh_token": 'YuGl5rueIghdXh0x8QLFWTz13C8kre',
                            "expires_in": datetime.datetime(
                                   2052, 2, 3, 12, 52, 0, 670849
                                   ).strftime('%Y-%m-%d %H:%M:%S')
        }
    json_presenter = PresenterImplementation()

    tokens_dict = json_presenter.get_log_in_user_response(
        tokens_dto=token_dto
    )

    assert tokens_dict == expected_tokens_dict
