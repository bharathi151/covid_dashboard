import pytest

from covid_dashboard.models import User
from covid_dashboard.storages.user_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_validate_password_given_valid_details_returns_true():
    user_name = "bharathi151273"
    password = "rgukt123"
    valid = True
    User.objects.create_user(name="bharathi", username="bharathi151273",password="rgukt123")
    sql_storage = StorageImplementation()

    user = User.objects.get(username=user_name)
    is_valid_password = sql_storage.validate_password(
        user_name=user_name, password=password
    )

    assert is_valid_password == valid

@pytest.mark.django_db
def test_validate_password_given_invalid_details_returns_false():
    user_name = "bharathi151273"
    password = "abc"
    invalid = False
    User.objects.create(name="bharathi", username="bharathi151273",password="rgukt123")
    sql_storage = StorageImplementation()

    is_valid_password = sql_storage.validate_password(
        user_name=user_name, password=password
    )

    assert is_valid_password == invalid
