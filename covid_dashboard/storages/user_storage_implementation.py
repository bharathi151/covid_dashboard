from abc import ABC
from abc import abstractmethod
from typing import Optional, List
from django.db.models import Count, Q, F, Prefetch
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

    def post_cases_details(self,
                           mandal_id: int,
                           date: date,
                           confirmed_cases: int,
                           recovered_cases: int,
                           deaths:int) -> int:
        stats_obj= CasesDetails.objects.create(
            date=date, mandal_id=mandal_id, recovered_cases=recovered_cases,
            confirmed_cases=confirmed_cases, deaths=deaths
        )
        stats_dto = CasesDetailsDto(
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
                             date: date,
                             mandal_id: int,
                             confirmed_cases:int,
                             recovered_cases:int,
                             deaths:int) -> CasesDetailsDto:
        stats = CasesDetails.objects.filter(mandal_id=mandal_id, date=date)
        stats.update(date=date, mandal_id=mandal_id,
                     confirmed_cases=confirmed_cases,
                     recovered_cases=recovered_cases,
                     deaths=deaths)
        stats_obj = CasesDetails.objects.get(mandal_id=mandal_id, date=date)
        stats_dto = CasesDetailsDto(
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