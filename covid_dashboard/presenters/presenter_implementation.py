from typing import List

from django_swagger_utils.drf_server.exceptions import (
    NotFound, Forbidden, Unauthorized, BadRequest
)
from covid_dashboard.constants.exception_messages import *
from covid_dashboard.interactors.presenters.presenter_interface import \
    PresenterInterface
from common.dtos import UserAuthTokensDTO
from covid_dashboard.interactors.storages.dtos import *

class PresenterImplementation(PresenterInterface):


    def raise_invalid_password_exception(self):
        raise BadRequest(*INVALID_PASSWORD)

    def raise_invalid_username_exception(self):
        raise NotFound(*INVALID_USER_NAME)

    def get_log_in_user_response(self, tokens_dto: UserAuthTokensDTO):
        tokens_dict = {
          "user_id": tokens_dto.user_id,
          "access_token": tokens_dto.access_token,
          "refresh_token": tokens_dto.refresh_token,
          "expires_in": tokens_dto.expires_in.strftime('%Y-%m-%d %H:%M:%S')
        }
        return tokens_dict

    def get_state_cumulative_details_dto_response(
        self, state_cumulative_dto: StateCumulativeDtos
    ):
        state = state_cumulative_dto.state
        districts =[district.__dict__ for district in state_cumulative_dto.districts]


        state_cumulative_dict = {
            "state_name": state.state_name,
            "total_confirmed_cases": state.total_confirmed_cases,
            "total_recovered_cases": state.total_recovered_cases,
            "total_deaths": state.total_deaths,
            "total_active_cases": state.total_active_cases,
            "districts": districts
        }
        return state_cumulative_dict

    def get_district_cumulative_details_dto_response(
        self, district_cumulative_dto: DistrictCumulativeDtos
        ):
        district = district_cumulative_dto.district
        mandals =[mandal.__dict__ for mandal in district_cumulative_dto.mandals]


        district_cumulative_dict = {
            "district_name": district.district_name,
            "district_id": district.district_id,
            "total_confirmed_cases": district.total_confirmed_cases,
            "total_recovered_cases": district.total_recovered_cases,
            "total_deaths": district.total_deaths,
            "total_active_cases": district.total_active_cases,
            "mandals": mandals
        }
        return district_cumulative_dict

    def get_day_wise_state_cumulative_details_dto_response(
        self, state_cumulative_dto: DayWiseStateCumulativeDtos
    ):
        day_wise_statistics = [ state.__dict__ for state in state_cumulative_dto.day_wise_statistics]
        day_wise_state_cumulative_dict = {
            "state_name": state_cumulative_dto.state_name,
            "day_wise_statistics": day_wise_statistics
        }
        return day_wise_state_cumulative_dict


    def get_day_wise_districts_cumulative_details_dto_response(
        self, districts_cumulative_dto: DayWiseDistrictCumulativeDtos
    ):
        districts_list = []
        for district_dto in districts_cumulative_dto.districts:
            day_wise_statistics_details = []
            for day_wise_district_dto in district_dto.day_wise_statistics:
                day_wise_district_details = {
                    "date": day_wise_district_dto.date,
                    "total_confirmed_cases": day_wise_district_dto.total_confirmed_cases,
                    "total_recovered_cases" : day_wise_district_dto.total_recovered_cases,
                    "total_deaths": day_wise_district_dto.total_deaths,
                    "total_active_cases": day_wise_district_dto.total_active_cases
                }
                day_wise_statistics_details.append(day_wise_district_details)
            districts_list.append({
                "district_name": district_dto.district_name,
                "district_id": district_dto.district_id,
                "day_wise_statistics": day_wise_statistics_details
            })
        return districts_list

    def get_day_wise_mandals_cumulative_details_dto_response(
        self, mandals_cumulative_dto: DayWiseMandalCumulativeDtos
    ):
        mandals_list = []
        for mandal_dto in mandals_cumulative_dto.mandals:
            day_wise_statistics_details = []
            for day_wise_mandal_dto in mandal_dto.day_wise_statistics:
                day_wise_mandal_details = {
                    "date": day_wise_mandal_dto.date,
                    "total_confirmed_cases": day_wise_mandal_dto.total_confirmed_cases,
                    "total_recovered_cases" : day_wise_mandal_dto.total_recovered_cases,
                    "total_deaths": day_wise_mandal_dto.total_deaths,
                    "total_active_cases": day_wise_mandal_dto.total_active_cases
                }
                day_wise_statistics_details.append(day_wise_mandal_details)
            mandals_list.append({
                "mandal_name": mandal_dto.mandal_name,
                "mandal_id": mandal_dto.mandal_id,
                "day_wise_statistics": day_wise_statistics_details
            })
        return mandals_list
    def raise_invalid_cases_details(self):
        raise BadRequest(*INVALID_CASES_DEATILS)

    def post_cases_details_response(self, stats_dto: CasesDetailsDto):
        return stats_dto.__dict__

    def update_cases_details_response(self, stats_dto: CasesDetailsDto):
        return stats_dto.__dict__

    def raise_invalid_mandal_id_exception(self):
        raise NotFound(*INVALID_MANDAL)

    def raise_invalid_district_id_exception(self):
        raise NotFound(*INVALID_DISTRICT)

    def raise_date_already_existed(self):
        raise BadRequest(*DATA_ALREADY_EXISTED)

    def raise_stats_not_existed(self):
        raise NotFound(*STATS_OBJECT_NOT_FOUND)

    def get_day_wise_district_cumulative_details_dto_response(
            self, district_cumulative_dto: DayWiseDistrictCumulativeDto):
        day_wise_statistics = [ district.__dict__ for district in district_cumulative_dto.day_wise_statistics]
        day_wise_district_cumulative_dict = {
            "district_name": district_cumulative_dto.district_name,
            "district_id": district_cumulative_dto.district_id,
            "day_wise_statistics": day_wise_statistics
        }
        return day_wise_district_cumulative_dict

    def get_state_daily_details_dto_response(self, state_daily_dto: StateTotalCasesDto):
        state = state_daily_dto
        districts =[district.__dict__ for district in state_daily_dto.districts]

        state_daily_dict = {
            "state_name": state.state_name,
            "total_confirmed_cases": state.total_confirmed_cases,
            "total_recovered_cases": state.total_recovered_cases,
            "total_deaths": state.total_deaths,
            "districts": districts
        }
        return state_daily_dict

    def get_district_daily_details_dto_response(
        self, district_daily_dto: DistrictTotalCasesDto
        ):
        district = district_daily_dto
        mandals =[mandal.__dict__ for mandal in district_daily_dto.mandals]


        district_daily_dict = {
            "district_name": district.district_name,
            "district_id": district.district_id,
            "total_confirmed_cases": district.total_confirmed_cases,
            "total_recovered_cases": district.total_recovered_cases,
            "total_deaths": district.total_deaths,
            "mandals": mandals
        }
        return district_daily_dict

    def get_day_wise_district_daily_details_dto_response(
        self, district_daily_dto: DayWiseDistrictTotalCasesDto):
        day_wise_statistics = [ district.__dict__ for district in district_daily_dto.day_wise_statistics]
        day_wise_district_daily_dict = {
            "district_name": district_daily_dto.district_name,
            "district_id": district_daily_dto.district_id,
            "day_wise_statistics": day_wise_statistics
        }
        return day_wise_district_daily_dict

    def get_day_wise_state_daily_details_dto_response(
        self, state_daily_dto: DayWiseStateTotalCasesDtos):
        day_wise_statistics = [ stats.__dict__ 
        for stats in state_daily_dto.day_wise_statistics
        ]
        day_wise_state_daily_dict = {
            "state_name": state_daily_dto.state_name,
            "day_wise_statistics": day_wise_statistics
        }
        return day_wise_state_daily_dict

    def get_day_wise_mandals_daily_details_dto_response(
            self, mandals_daily_dto: DayWiseMandalTotalCasesDtos):
        mandals_list = []
        for mandal_dto in mandals_daily_dto.mandals:
            day_wise_statistics_details = []
            for day_wise_mandal_dto in mandal_dto.day_wise_statistics:
                day_wise_mandal_details = {
                    "date": day_wise_mandal_dto.date,
                    "total_confirmed_cases": day_wise_mandal_dto.total_confirmed_cases,
                    "total_recovered_cases" : day_wise_mandal_dto.total_recovered_cases,
                    "total_deaths": day_wise_mandal_dto.total_deaths
                }
                day_wise_statistics_details.append(day_wise_mandal_details)
            mandals_list.append({
                "mandal_name": mandal_dto.mandal_name,
                "mandal_id": mandal_dto.mandal_id,
                "day_wise_statistics": day_wise_statistics_details
            })
        return mandals_list

    def get_mandal_stats_dto_response(self, stats_dto):
        stats = [ day_stats.__dict__ 
            for day_stats in stats_dto.stats
        ]
        return stats

    def get_districts_zones_dto_response(
            self, zones_dto: DistrictZones):
        zones = [ district_zone.__dict__ 
            for district_zone in zones_dto.zones
        ]
        return zones