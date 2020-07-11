from abc import ABC
from abc import abstractmethod
from typing import Optional, List
from django.db.models import Sum, Count, Q, F, Prefetch
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.interactors.storages.user_storage_interface import StorageInterface
from covid_dashboard.models import *

class StorageImplementation(StorageInterface):

    def validate_username(self, user_name: str) -> bool:
        try:
            User.objects.get(username=user_name)
        except User.DoesNotExist:
            return False
        return True

    def validate_password(self, user_name: str, password: str) -> bool:

        user = User.objects.get(username=user_name)

        valid_password = user.check_password(password)
        if valid_password:
            return True
        return False

    def get_user_id(self, user_name: str, password: str) -> int:

        user = User.objects.get(username=user_name)
        user_id = user.id
        return user_id

    def sign_up(self, user_name: str, password:str, confirm_password: str) -> int:
        user = User.objects.create_user(
            username=user_name,
            password=password,
            name=user_name
        )
        user_name = user.username
        password = user.password
        return user_name,password

    def is_valid_cases_details(self,
                                 confirmed_cases: int,
                                 recovered_cases: int,
                                 deaths: int):
        casesdetails = CasesDetails.objects.filter(mandal__district__state_id=1). \
            values(
                'mandal__district__state_id','mandal__district__state__state_name'
                ).annotate(
                total_confirmed_cases=Sum(
                    'confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'recovered_cases'
                ),
                total_deaths=Sum(
                    'deaths'
                )
            )
        if casesdetails:
            total_confirmed_cases = casesdetails[0]['total_confirmed_cases']
            total_recovered_cases = casesdetails[0]['total_recovered_cases']
            total_deaths = casesdetails[0]['total_deaths']
        else:
            total_confirmed_cases = 0
            total_recovered_cases = 0
            total_deaths = 0

        total_confirmed_cases = total_confirmed_cases + confirmed_cases
        total_recovered_cases = total_recovered_cases + recovered_cases
        total_deaths = total_deaths + deaths
        if total_confirmed_cases < (total_recovered_cases+total_deaths):
            return False
        return True

    def post_cases_details(self,
                           cases_details_dto: CasesDetailsDto) -> PostCasesDetailsDto:
        stats_obj= CasesDetails.objects.create(
            date=cases_details_dto.date, mandal_id=cases_details_dto.mandal_id,
            recovered_cases=cases_details_dto.recovered_cases,
            confirmed_cases=cases_details_dto.confirmed_cases,
            deaths=cases_details_dto.deaths
        )
        stats_dto = PostCasesDetailsDto(
            mandal_id=stats_obj.mandal_id,
            date=stats_obj.date.strftime("%d/%m/%Y"),
            total_confirmed_cases=stats_obj.confirmed_cases,
            total_recovered_cases=stats_obj.recovered_cases,
            total_deaths=stats_obj.deaths
            )
        return stats_dto

    def is_valid_mandal_id(self,  mandal_id):
        try:
            Mandal.objects.get(id=mandal_id)
        except Mandal.DoesNotExist:
            return False
        return True

    def is_mandal_data_for_date_already_existed(self, date: str, mandal_id: int) -> bool:
        try:
            CasesDetails.objects.get(mandal_id=mandal_id, date=date)
        except CasesDetails.DoesNotExist:
            return False
        return True

    def update_cases_details(self,
                             cases_details_dto: CasesDetailsDto) -> PostCasesDetailsDto:
        CasesDetails.objects.filter(
            mandal_id=cases_details_dto.mandal_id, date=cases_details_dto.date
            ).update(
                date=cases_details_dto.date,
                mandal_id=cases_details_dto.mandal_id,
                confirmed_cases=cases_details_dto.confirmed_cases,
                recovered_cases=cases_details_dto.recovered_cases,
                deaths=cases_details_dto.deaths
            )
        stats_obj = CasesDetails.objects.get(
            mandal_id=cases_details_dto.mandal_id, date=cases_details_dto.date
        )
        stats_dto = PostCasesDetailsDto(
            mandal_id=stats_obj.mandal_id,
            date=stats_obj.date.strftime("%d/%m/%Y"),
            total_confirmed_cases=stats_obj.confirmed_cases,
            total_recovered_cases=stats_obj.recovered_cases,
            total_deaths=stats_obj.deaths
            )
        return stats_dto

    def get_mandal_stats_dto(self):
        stats = CasesDetails.objects.all().select_related('mandal').prefetch_related('mandal__district')
        stats_dtos = []
        for day_stats in stats:
            day_stats_dto = DayStats(
                date = day_stats.date.strftime("%d/%m/%Y"),
                district_name = day_stats.mandal.district.district_name,
                mandal_name = day_stats.mandal.mandal_name,
                total_confirmed_cases = day_stats.confirmed_cases,
                total_recovered_cases = day_stats.recovered_cases,
                total_deaths = day_stats.deaths,
                total_active_cases = day_stats.confirmed_cases - (
                    day_stats.recovered_cases + day_stats.deaths)
            )
            stats_dtos.append(day_stats_dto)
        stats_dto = StatsDtos(
            stats = stats_dtos
        )
        return stats_dto