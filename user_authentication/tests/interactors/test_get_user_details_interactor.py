from unittest.mock import create_autospec

from user_authentication.interactors.storages.dtos import UserDTO
from user_authentication.interactors.get_user_details_interactor import \
    GetUserDetailsInteractor
from user_authentication.interactors.storages.storage_interface import \
    StorageInterface


class TestGetUserDetailsInteractor:

    def test_given_user_ids_then_return_user_details_dto(self):
        user_ids = [1, 2]
        expected_user_details_dtos = [
            UserDTO(
                user_id=1,
                name="name1",
                profile_pic_url="url1"
            ),
            UserDTO(
                user_id=2,
                name="name1",
                profile_pic_url="url1"
            )
        ]
        storage = create_autospec(StorageInterface)
        storage.get_user_details_dtos.return_value = expected_user_details_dtos
        interactor = GetUserDetailsInteractor(storage=storage)

        actual_user_details_dto = interactor.get_user_details_wrapper(
            user_ids=user_ids)

        assert actual_user_details_dto == expected_user_details_dtos
        storage.get_user_details_dtos.assert_called_once_with(
            user_ids=user_ids)
