import pytest
import datetime

from covid_dashboard.models import CasesDetails
from covid_dashboard.storages.user_storage_implementation import StorageImplementation

@pytest.mark.django_db
def test_is_valid_mandal_id_invalid_details_return_false():
    mandal_id=1
    invalid = False
    sql_storage = StorageImplementation()

    is_valid_mandal_id = sql_storage.is_valid_mandal_id(
        mandal_id=mandal_id)

    assert is_valid_mandal_id == invalid
