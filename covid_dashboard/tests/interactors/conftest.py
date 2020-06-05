import datetime

import pytest
from covid_dashboard.interactors.storages.dtos import *

@pytest.fixture()
def create_state():
    state = StateDto(
        state_name="AndhraPradesh",
        state_id=1
    )
    return state

@pytest.fixture()
def create_districts():
    districts = [
        DistrictDto(
            district_name="Kadapa",
            district_id=1,
            state_id=1
        ),
        DistrictDto(
            district_name="Kurnool",
            district_id=2,
            state_id=1
        ),
    ]
    return districts

@pytest.fixture()
def create_mandals():
    mandals = [
        MandalDto(
            mandal_name="rayachoty",
            mandal_id=1,
            district_id=1
        ),
        MandalDto(
            mandal_name="bethamcharla",
            mandal_id=2,
            district_id=2
        ),
    ]
    return mandals

@pytest.fixture()
def create_kadapa_mandals():
    mandals = [
        MandalDto(
            mandal_name="Rayachoty",
            mandal_id=1,
            district_id=1
        ),
        MandalDto(
            mandal_name="Gaaliveedu",
            mandal_id=2,
            district_id=1
        ),
    ]
    return mandals

@pytest.fixture()
def get_state_cumulative_response():
    get_state_cumulative_response = {
        "state_name": "AndhraPradesh",
        "total_confirmed_cases": 700,
        "total_recovered_cases": 200,
        "total_deaths": 100,
        "total_active_cases": 400,
        "districts": [
            {
                "district_name": "Kadapa",
                "district_id": 1,
                "total_confirmed_cases": 200,
                "total_recovered_cases": 80,
                "total_deaths": 30,
                "total_active_cases": 90
            },
            {
                "district_name": "Kurnool",
                "district_id": 2,
                "total_confirmed_cases": 500,
                "total_recovered_cases": 120,
                "total_deaths": 70,
                "total_active_cases": 310
            }
        ]
    }
    return get_state_cumulative_response

@pytest.fixture()
def get_district_cumulative_response():
    get_district_cumulative_response = {
        "district_name": "Kadapa",
        "district_id": 1,
        "total_confirmed_cases": 20,
        "total_recovered_cases": 4,
        "total_deaths": 2,
        "total_active_cases": 14,
        "districts": [
            {
                "mandal_name": "Rayachoty",
                "mandal_id": 1,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            },
            {
                "mandal_name": "Gaaliveedu",
                "mandal_id": 2,
                "total_confirmed_cases": 10,
                "total_recovered_cases": 2,
                "total_deaths": 1,
                "total_active_cases": 7
            }
        ]
    }
    return get_district_cumulative_response