import datetime

import pytest
from freezegun import freeze_time

from covid_dashboard.models import *


@pytest.fixture()
def create_users():
    users = [
        {
            'username': 'bharathi151273',
            "name": "bharathi",
            "password": "rgukt123"
        }
    ]
    for user in users:
        User.objects.create(
            username=user['username'],
            name=user['name'],
            password=user['password'])

@pytest.fixture()
def create_state():
    State.objects.create(state_name="AndhraPradesh")

@pytest.fixture()
def create_districts(create_state):
    District.objects.create(state_id=1, district_name="Kadapa")
    District.objects.create(state_id=1, district_name="Kurnool")

@pytest.fixture()
def create_mandals(create_districts):
     Mandal.objects.create(district_id=1, mandal_name="Rayachoty")
     Mandal.objects.create(district_id=2, mandal_name="Nandyala")

@pytest.fixture()
def create_kadapa_mandals(create_districts):
     Mandal.objects.create(district_id=1, mandal_name="Rayachoty")
     Mandal.objects.create(district_id=1, mandal_name="Gaaliveedu")

@pytest.fixture()
def kadapa_mandals(create_district):
     Mandal.objects.create(district_id=1, mandal_name="Rayachoty")
     Mandal.objects.create(district_id=1, mandal_name="Gaaliveedu")

@pytest.fixture()
def post_cases(create_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,22),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=2
    )

@pytest.fixture()
def kadapa_mandals_post_cases(create_kadapa_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,22),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=2
    )

@pytest.fixture()
def kadapa_cases(kadapa_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=2
    )

@pytest.fixture()
def daily_cases(create_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,21),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=2
    )

@pytest.fixture()
def mandals_cases(kadapa_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,21),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=2
    )

@pytest.fixture()
def cases(create_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )

@pytest.fixture()
def rayachoty_cases(create_kadapa_mandals):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )


@pytest.fixture()
def create_district(create_state):
    District.objects.create(state_id=1, district_name="Kadapa")

@pytest.fixture()
def create_mandal(create_district):
     Mandal.objects.create(district_id=1, mandal_name="Rayachoty")

@pytest.fixture()
def district_daily_cases(create_mandal):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,21),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )

@pytest.fixture()
def cases_for_update(create_mandal):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,30),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )

@pytest.fixture()
def district_cases(create_mandal):
    CasesDetails.objects.create(
        date=datetime.date(2020,5,20),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )
    CasesDetails.objects.create(
        date=datetime.date(2020,5,22),
        confirmed_cases = 10,
        recovered_cases = 2,
        deaths = 1,
        mandal_id=1
    )