from abc import ABC
import datetime
from abc import abstractmethod
from typing import Optional, List
from django.db.models import Sum, F
from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.interactors.storages.storage_interface import StorageInterface

class StorageImplementation(StorageInterface):
    def is_valid_district_id(self, district_id: int) -> bool:
        try:
            District.objects.get(id=district_id)
        except District.DoesNotExist:
            return False
        return True

    def get_district_cumulative_details_dto(self, till_date: date, district_id) -> DistrictTotalCasesDtos:
        mandals_query_set = Mandal.objects.filter(
            casesdetails__date__lte=till_date, district_id=district_id). \
            values('district_id','district__district_name', 'id', 'mandal_name').annotate(
                total_confirmed_cases=Sum(
                    'casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'casesdetails__deaths'
                )
            )
        if mandals_query_set:
            district_total_cases_dto = self._get_district_total_cases_dto(
                mandals_query_set, district_id
            )
        else: 
           district_total_cases_dto = self._get_district_total_cases_dto_with_zeros(district_id)
            
        return district_total_cases_dto

    def _get_district_total_cases_dto(self, mandals_query_set, district_id):
        mandal_objs = Mandal.objects.filter(district_id=district_id)
        mandals_dtos_ids=[obj["id"] for obj in mandals_query_set]
        mandal_total_cases_dtos=[]
        for obj in mandal_objs:
            is_id_existed = obj.id in mandals_dtos_ids
            if is_id_existed:
                mandal_total_cases_dtos.append(
                    self._update_cases_count_with_mandal_counts(
                        obj.id, mandals_query_set
                    )
                )
            else:
                mandal_total_cases_dtos.append(
                    self._update_cases_count_with_zeros(obj)
                )
        district_total_cases_dto = self._construct_ditrict_total_cases_dto(mandal_total_cases_dtos,mandals_query_set)
        return district_total_cases_dto

    def _construct_ditrict_total_cases_dto(self, mandal_total_cases_dtos, mandals_query_set):
        total_confirmed_cases = 0
        total_recovered_cases = 0
        total_deaths = 0
        for mandal_dto in mandal_total_cases_dtos:
            total_confirmed_cases += mandal_dto.total_confirmed_cases
            total_recovered_cases += mandal_dto.total_recovered_cases
            total_deaths += mandal_dto.total_deaths
        district_total_cases_dto = DistrictTotalCasesDtos(
              district_name=mandals_query_set[0]["district__district_name"],
              district_id=mandals_query_set[0]["district_id"],
              total_confirmed_cases=total_confirmed_cases,
              total_recovered_cases=total_recovered_cases,
              total_deaths=total_deaths,
              mandals=mandal_total_cases_dtos
        )
        return district_total_cases_dto

    def _update_cases_count_with_mandal_counts(self, id, mandals_query_set):
        for mandal_obj in mandals_query_set:
            if id == mandal_obj["id"]:
                mandal=mandal_obj
        mandal_dto = MandalTotalCasesDto(
            mandal_name=mandal["mandal_name"],
            mandal_id=mandal["id"],
            total_confirmed_cases=mandal["total_confirmed_cases"],
            total_recovered_cases=mandal["total_recovered_cases"],
            total_deaths=mandal["total_deaths"]
        )
        return mandal_dto

    def _update_cases_count_with_zeros(self, mandal):
        mandal_dto = MandalTotalCasesDto(
            mandal_name=mandal.mandal_name,
            mandal_id=mandal.id,
            total_confirmed_cases=0,
            total_recovered_cases=0,
            total_deaths=0
        )
        return mandal_dto

    def _get_district_total_cases_dto_with_zeros(self, district_id):
        mandals_objs = Mandal.objects.filter(district_id=district_id).select_related('district')
        mandals_total_cases_dtos = []
        for mandal in mandals_objs:
            mandals_total_cases_dtos.append(
                self._update_cases_count_with_zeros(mandal)
            )
        district_total_cases_dto = DistrictTotalCasesDtos(
              district_name=mandals_objs[0].district.district_name,
              district_id=mandals_objs[0].district_id,
              total_confirmed_cases=0,
              total_recovered_cases=0,
              total_deaths=0,
              mandals=mandals_total_cases_dtos
        )
        return district_total_cases_dto

    def get_day_wise_district_cumulative_dto(self, district_id: int) -> DayWiseDistrictTotalCasesDto:
        district_details_objs = Mandal.objects.filter(
            casesdetails__date__isnull=False,district_id=district_id
            ). \
            values('district_id', 'district__district_name', 'casesdetails__date'). \
            annotate(
                total_confirmed_cases=Sum('casesdetails__confirmed_cases'),
                total_recovered_cases=Sum('casesdetails__recovered_cases'),
                total_deaths=Sum('casesdetails__deaths')
            )

        district_details_objs_ids = [district["district_id"] for district in district_details_objs]
        if district_details_objs:
            district_details_objs_dates = [district["casesdetails__date"] for district in district_details_objs]
            day_wise_statistics =self._get_day_wise_statistics_dtos(
                district_details_objs, district_details_objs_dates)
        else:
            district_details_objs_dates = Mandal.objects.filter(
            casesdetails__date__isnull=False
            ).values_list('casesdetails__date',flat=True)
    
            day_wise_statistics =self._get_day_wise_statistics_dtos_with_zeros(
                district_details_objs, district_details_objs_dates)

        if district_id in district_details_objs_ids:
            districts = district_details_objs.filter(district_id=district_id)
            day_wise_district_total_cases_dto = DayWiseDistrictTotalCasesDto(
                    district_name=districts[0]["district__district_name"],
                    district_id=districts[0]["district_id"],
                    day_wise_statistics=day_wise_statistics
                )
        else:
            district = District.objects.get(id=district_id)
            day_wise_district_total_cases_dto = DayWiseDistrictTotalCasesDto(
                    district_name=district.district_name,
                    district_id=district.id,
                    day_wise_statistics=day_wise_statistics
                )

        return day_wise_district_total_cases_dto

    def _get_day_wise_statistics_dtos_with_zeros(self, district_objs, dates):
        total_confirmed_cases = 0
        total_recovered_cases = 0
        total_deaths = 0
        day_wise_statistics = []
        if not dates:
            return day_wise_statistics
        min_date = min(dates)
        max_date = max(dates)
        delta = datetime.timedelta(days=1)
        while min_date<=max_date:
            day_wise_statistics.append(
                self._get_day_wise_statistics_dto(
                    min_date, total_recovered_cases,
                    total_confirmed_cases, total_deaths
                )
            )
            min_date += delta
        return day_wise_statistics

    def _get_day_wise_statistics_dtos(self, district_objs, dates):
        total_confirmed_cases = 0
        total_recovered_cases = 0
        total_deaths = 0
        day_wise_statistics = []
        if not dates:
            return day_wise_statistics
        min_date = min(dates)
        max_date = max(dates)
        delta = datetime.timedelta(days=1)
        while min_date<=max_date:
            if min_date not in dates:
                day_wise_statistics.append(
                    self._get_day_wise_statistics_dto(
                        min_date, total_recovered_cases,
                        total_confirmed_cases, total_deaths
                    )
                )
            else:
                for district in district_objs:
                    if district["casesdetails__date"] == min_date:
                        total_confirmed_cases += district["total_confirmed_cases"]
                        total_recovered_cases += district["total_recovered_cases"] 
                        total_deaths += district["total_deaths"]
                        date = district["casesdetails__date"]
                        day_wise_statistics.append(
                            self._get_day_wise_statistics_dto(
                                date, total_recovered_cases,
                                total_confirmed_cases, total_deaths
                            )
                        )
            min_date+=delta
        return day_wise_statistics

    def _get_day_wise_statistics_dto(self, date, total_recovered_cases,
                                     total_confirmed_cases, total_deaths
    ):
        day_statistics_dto = DayWiseTotalCasesDto(
            date=date.strftime("%d/%m/%Y"),
            total_confirmed_cases=total_confirmed_cases,
            total_recovered_cases=total_recovered_cases,
            total_deaths=total_deaths
        )
        return day_statistics_dto

    def get_day_wise_mandals_cumulative_dto(self, district_id: int) -> DayWiseMandalTotalCasesDtos:
        mandal_objs = Mandal.objects.filter(district_id=district_id). \
             values('id', 'mandal_name', 'casesdetails__date'). \
             annotate(
                 total_confirmed_cases=Sum('casesdetails__confirmed_cases'),
                 total_recovered_cases=Sum('casesdetails__recovered_cases'),
                 total_deaths=Sum('casesdetails__deaths')
             )
        mandals_total_cases_dto = self._get_mandals_day_wise_stats_dto(mandal_objs)
        return mandals_total_cases_dto

    def _get_mandals_day_wise_stats_dto(self, mandal_objs):
        mandals_ids = []
        mandals_dates = []
        for mandal in mandal_objs:
            if mandal["casesdetails__date"]:
                if mandal["casesdetails__date"] not in mandals_dates:
                    mandals_dates.append(mandal["casesdetails__date"])
        for mandal in mandal_objs:
            if mandal["id"] not in mandals_ids:
                mandals_ids.append(mandal["id"])
        mandals_dtos = self._get_day_wise_mandals_cumulative_stats_dtos(
                mandal_objs, mandals_ids, mandals_dates
            )
        mandals_total_cases_dto = DayWiseMandalTotalCasesDtos(
            mandals=mandals_dtos
        )
        return mandals_total_cases_dto

    def _get_day_wise_mandals_cumulative_stats_dtos(self, mandal_objs,
                                                mandals_ids, mandals_dates):
        mandals = []
        if not mandals_dates:
            return mandals
        min_date = min(mandals_dates)
        max_date = max(mandals_dates)
        delta = datetime.timedelta(days=1)

        for id in mandals_ids:
            total_confirmed_cases = 0
            total_recovered_cases = 0
            total_deaths = 0
            day_wise_total_cases_dtos = []
            min_date = min(mandals_dates)
            while min_date<=max_date:
                for mandal in mandal_objs:
                    if id == mandal["id"] and min_date == mandal["casesdetails__date"] :
                        total_confirmed_cases += mandal["total_confirmed_cases"]
                        total_recovered_cases += mandal["total_recovered_cases"]
                        total_deaths += mandal["total_deaths"]
                date = min_date
                day_wise_total_cases_dtos.append(
                    self._get_mandal_day_total_cases_dto(
                        total_confirmed_cases, total_recovered_cases,
                        total_deaths, date
                    )
                )
                min_date += delta
            mandals.append(
                        self._get_day_wise_mandal_cumulative_dto(
                            day_wise_total_cases_dtos, id, mandal_objs
                        )
                    )
        return mandals
    def _get_mandal_day_total_cases_dto(
        self, total_confirmed_cases, total_recovered_cases, total_deaths, date):
        day_wise_total_cases_dto = DayWiseTotalCasesDto(
            date=date.strftime("%d/%m/%Y"),
            total_confirmed_cases=total_confirmed_cases,
            total_recovered_cases=total_recovered_cases,
            total_deaths=total_deaths
        )
        return day_wise_total_cases_dto

    def _get_day_wise_mandal_cumulative_dto(self, 
                                              day_wise_total_cases_dtos,
                                              id, mandal_objs):
        mandal_name = None
        for mandal in mandal_objs:
            if id == mandal["id"]:
                mandal_name = mandal["mandal_name"]
                break
        day_wise_mandal_dto = DayWiseMandalTotalCasesDto(
            mandal_name=mandal_name,
            mandal_id=id,
            day_wise_statistics=day_wise_total_cases_dtos
        )
        return day_wise_mandal_dto

    def get_district_daily_details_dto(self, date: date, district_id: int) -> DistrictTotalCasesDto:
        mandals_query_set = Mandal.objects.filter(
            casesdetails__date=date, district_id=district_id). \
            values('district_id','district__district_name', 'id', 'mandal_name').annotate(
                total_confirmed_cases=F(
                    'casesdetails__confirmed_cases'
                ),
                total_recovered_cases=F(
                    'casesdetails__recovered_cases'
                ),
                total_deaths=F(
                    'casesdetails__deaths'
                )
            )
        if mandals_query_set:
            district_total_cases_dto = self._get_district_total_cases_dto(
                mandals_query_set, district_id
            )
        else: 
           district_total_cases_dto = self._get_district_total_cases_dto_with_zeros(district_id)
            
        return district_total_cases_dto

    def get_day_wise_district_daily_dto(self, district_id: int, till_date: str) -> DayWiseDistrictTotalCasesDto:
        district_details_objs = Mandal.objects.filter(
            casesdetails__date__lte=till_date,district_id=district_id
            ). \
            values('district_id', 'district__district_name', 'casesdetails__date'). \
            annotate(
                total_confirmed_cases=Sum('casesdetails__confirmed_cases'),
                total_recovered_cases=Sum('casesdetails__recovered_cases'),
                total_deaths=Sum('casesdetails__deaths')
            )

        dates = CasesDetails.objects.filter(date__lte=till_date).values_list('date', flat=True)
        dates_not_existed = not dates
        if dates_not_existed:
            district_name = District.objects.get(id=district_id).district_name
            day_wise_district_total_cases_dto = DayWiseDistrictTotalCasesDto(
                    district_name=district_name,
                    district_id=district_id,
                    day_wise_statistics=[]
            )
            return day_wise_district_total_cases_dto
        day_wise_statistics = self._get_day_wise_stats(
            dates, district_details_objs, till_date
        )
        day_wise_district_total_cases_dto = DayWiseDistrictTotalCasesDto(
                    district_name=district_details_objs[0]["district__district_name"],
                    district_id=district_details_objs[0]["district_id"],
                    day_wise_statistics=day_wise_statistics
        )
        return day_wise_district_total_cases_dto

    def _get_day_wise_stats(self, dates, district_details_objs, till_date):
        start_date = min(dates)
        district_obj_date_wise_stats = {}
        district_obj_dates=[]
        delta = datetime.timedelta(days=1)
        for obj in district_details_objs:
            date = obj["casesdetails__date"]
            district_obj_dates.append(date)
            district_obj_date_wise_stats[date] = obj

        day_wise_statistics = []
        while start_date <= till_date:
            if start_date in district_obj_dates:
                obj = district_obj_date_wise_stats[start_date]
                total_confirmed_cases = obj["total_confirmed_cases"]
                total_recovered_cases = obj["total_recovered_cases"]
                total_deaths = obj["total_deaths"]
            else:
                total_confirmed_cases = 0
                total_recovered_cases = 0
                total_deaths = 0
            day_wise_statistics.append(
                    self._get_day_wise_statistics_dto(
                        start_date, total_recovered_cases,
                        total_confirmed_cases, total_deaths
                    )
            )
            start_date += delta
        return day_wise_statistics

    def get_day_wise_mandals_daily_dto(self, district_id: int,
                                       till_date: str):
        mandal_objs = Mandal.objects.filter(
            district_id=district_id,casesdetails__date__lte=till_date
            ). \
             values('id', 'mandal_name', 'casesdetails__date'). \
             annotate(
                 total_confirmed_cases=F('casesdetails__confirmed_cases'),
                 total_recovered_cases=F('casesdetails__recovered_cases'),
                 total_deaths=F('casesdetails__deaths')
             )
        mandals_total_cases_dto = self._get_mandals_day_wise_stats_dto(mandal_objs)
        return mandals_total_cases_dto
