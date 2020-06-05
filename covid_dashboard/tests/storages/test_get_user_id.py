import pytest

from covid_dashboard.models import User
from covid_dashboard.storages.user_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_get_user_id_given_valid_details_returns_user_id(
        create_users
    ):
    user_name = "bharathi151273"
    password = "rgukt123"
    expected_user_id = 1
    sql_storage = StorageImplementation()

    user_id = sql_storage.get_user_id(
        user_name=user_name, password=password
    )

    assert user_id == expected_user_id
