import pytest

from covid_dashboard.models import User
from covid_dashboard.storages.user_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_user_name_given_valid_details_returns_true(
        create_users
    ):
    user_name = "bharathi151273"
    password = "rgukt123"
    valid = True
    sql_storage = StorageImplementation()

    is_valid_user_name = sql_storage.validate_username(user_name=user_name)

    assert is_valid_user_name == valid

@pytest.mark.django_db
def test_validate_user_name_given_invalid_details_returns_false(
        create_users
    ):
    user_name = "bharathi151"
    password = "rgukt123"
    invalid = False
    sql_storage = StorageImplementation()

    is_valid_user_name = sql_storage.validate_username(user_name=user_name)

    assert is_valid_user_name == invalid
