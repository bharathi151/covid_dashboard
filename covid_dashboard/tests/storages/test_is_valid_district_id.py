import pytest
import datetime

from covid_dashboard.models import District
from covid_dashboard.storages.district_storage_implementation import StorageImplementation

@pytest.mark.django_db
def test_is_valid_mandal_id_given_invalid_details_return_false():
    district_id=1
    invalid = False
    sql_storage = StorageImplementation()

    is_valid_district_id = sql_storage.is_valid_district_id(
        district_id=district_id)

    assert is_valid_district_id == invalid
