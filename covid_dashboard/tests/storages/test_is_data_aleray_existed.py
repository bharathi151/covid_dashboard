import pytest
import datetime

from covid_dashboard.models import CasesDetails
from covid_dashboard.storages.user_storage_implementation import StorageImplementation

@pytest.mark.django_db
def test_post_cases_given_existed_details_return_true(post_cases):
    mandal_id=1
    date = "2020-5-20"
    existed = True
    sql_storage = StorageImplementation()

    is_data_existed = sql_storage.is_mandal_data_for_date_already_existed(
        date=date, mandal_id=mandal_id)

    assert is_data_existed == existed
