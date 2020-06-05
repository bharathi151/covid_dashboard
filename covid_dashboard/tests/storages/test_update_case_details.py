import pytest
import datetime

from covid_dashboard.models import CasesDetails
from covid_dashboard.storages.user_storage_implementation import StorageImplementation


@pytest.mark.django_db
def test_update_cases_given_valid_details_updates_cases(cases_for_update):
    mandal_id=1
    confirmed_cases=2
    deaths=0
    recovered_cases=1
    date = datetime.date(2020,5,30)
    sql_storage = StorageImplementation()

    stats_dto = sql_storage.update_cases_details(
        mandal_id=mandal_id,
        date=date,
        confirmed_cases=confirmed_cases,
        
        deaths=deaths,
        recovered_cases=recovered_cases)


    assert stats_dto.date == date
    assert stats_dto.total_recovered_cases == recovered_cases
    assert stats_dto.total_confirmed_cases == confirmed_cases
    assert stats_dto.total_deaths == deaths
    assert stats_dto.mandal_id == mandal_id
