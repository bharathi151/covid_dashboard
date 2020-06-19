from abc import ABC
import datetime
from abc import abstractmethod
from typing import Optional, List
from django.db.models import Sum, F
from collections import defaultdict 
from covid_dashboard.models import *
from covid_dashboard.interactors.storages.dtos import *
from covid_dashboard.interactors.storages.state_storage_interface import StorageInterface

class StorageImplementation(StorageInterface):

    def get_state_cumulative_details_dto(self, till_date: date) -> StateTotalCasesDto:
        state_dto = District.objects.filter(
            mandals__casesdetails__date__lte=till_date,state_id=1). \
            values('state_id','state__state_name').annotate(
                total_confirmed_cases=Sum(
                    'mandals__casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'mandals__casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'mandals__casesdetails__deaths'
                )
            )
        districts_query_set = District.objects.filter(
            mandals__casesdetails__date__lte=till_date). \
            values('id','district_name').annotate(
                total_confirmed_cases=Sum(
                    'mandals__casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'mandals__casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'mandals__casesdetails__deaths'
                )
            )
        if districts_query_set:
            state_total_cases_dto = self._get_state_total_cases_dto(state_dto, districts_query_set)
        else: 
           state_total_cases_dto = self._get_state_total_cases_dto_with_zeros()
            
        return state_total_cases_dto

    def _get_state_total_cases_dto(self, state_dto, districts_query_set):
        district_objs = District.objects.all()
        district_objs_dict = {}
        for obj in districts_query_set:
            district_objs_dict[obj["id"]] = obj
        districts_dtos_ids=[obj["id"]for obj in districts_query_set]
        district_total_cases_dtos=[]
        for obj in district_objs:
            if obj.id in districts_dtos_ids:
                district_total_cases_dtos.append(
                    self._update_cases_count_with_obj_count(
                        obj.id, district_objs_dict
                    )
                )
            else:
                district_total_cases_dtos.append(
                    self._update_cases_count_with_zeros(obj)
                )

        state_total_cases_dto = StateTotalCasesDto(
              state_name=state_dto[0]["state__state_name"],
              total_confirmed_cases=state_dto[0]["total_confirmed_cases"],
              total_recovered_cases=state_dto[0]["total_recovered_cases"],
              total_deaths=state_dto[0]["total_deaths"],
              districts=district_total_cases_dtos
        )
        return state_total_cases_dto

    def _update_cases_count_with_obj_count(self, id, district_objs_dict):
        district=district_objs_dict[id]
        district_dto = DistrictTotalCasesDto(
            district_name=district["district_name"],
            district_id=district["id"],
            total_confirmed_cases=district["total_confirmed_cases"],
            total_recovered_cases=district["total_recovered_cases"],
            total_deaths=district["total_deaths"]
        )
        return district_dto

    def _update_cases_count_with_zeros(self, district):
        district_dto = DistrictTotalCasesDto(
            district_name=district.district_name,
            district_id=district.id,
            total_confirmed_cases=0,
            total_recovered_cases=0,
            total_deaths=0
        )
        return district_dto

    def _get_state_total_cases_dto_with_zeros(self):
        districts_objs = District.objects.filter(state_id=1).select_related('state')
        districts_total_cases_dtos = []
        for district in districts_objs:
            districts_total_cases_dtos.append(
                self._update_cases_count_with_zeros(district)
            )
        state_total_cases_dto = StateTotalCasesDto(
              state_name=districts_objs[0].state.state_name,
              total_confirmed_cases=0,
              total_recovered_cases=0,
              total_deaths=0,
              districts=districts_total_cases_dtos
        )
        return state_total_cases_dto


    def get_day_wise_state_cumulative_dto(self) -> DayWiseStateTotalCasesDtos:
        state_details_objs = District.objects.filter(
            mandals__casesdetails__date__isnull=False
            ). \
            values('state_id', 'state__state_name', 'mandals__casesdetails__date'). \
            annotate(
                total_confirmed_cases=Sum('mandals__casesdetails__confirmed_cases'),
                total_recovered_cases=Sum('mandals__casesdetails__recovered_cases'),
                total_deaths=Sum('mandals__casesdetails__deaths')
            )
        state_objs_dict = {}
        for obj in state_details_objs:
            state_objs_dict[obj["mandals__casesdetails__date"]] = obj
        state_details_objs_dates = [state["mandals__casesdetails__date"] for state in state_details_objs]
        day_wise_statistics =self._get_day_wise_statistics_dtos(
            state_details_objs, state_details_objs_dates, state_objs_dict
        )
        day_wise_state_cumulative_dto = self._get_day_wise_state_cumulative_dto(state_details_objs, day_wise_statistics)
        return day_wise_state_cumulative_dto

    def _get_day_wise_state_cumulative_dto(self, state_details_objs, day_wise_statistics):
        if state_details_objs:
            day_wise_state_cumulative_dto = DayWiseStateTotalCasesDtos(
                    state_name=state_details_objs[0]["state__state_name"],
                    day_wise_statistics=day_wise_statistics
                )
        else:
            state=State.objects.get(id=1)
            day_wise_state_cumulative_dto = DayWiseStateTotalCasesDtos(
                state_name=state.state_name,
                day_wise_statistics=[]
            )

        return day_wise_state_cumulative_dto

    def _get_day_wise_statistics_dtos(self, state_objs, dates, state_objs_dict):
        state_objs_dict = {}
        for obj in state_objs:
            state_objs_dict[obj["mandals__casesdetails__date"]] = obj
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
                state = state_objs_dict[min_date]
                total_confirmed_cases += state["total_confirmed_cases"]
                total_recovered_cases += state["total_recovered_cases"] 
                total_deaths += state["total_deaths"]
                date = state["mandals__casesdetails__date"]
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
        day_statistics_dto = DayWiseStateTotalCasesDto(
            date=date.strftime("%d/%m/%Y"),
            total_confirmed_cases=total_confirmed_cases,
            total_recovered_cases=total_recovered_cases,
            total_deaths=total_deaths
        )
        return day_statistics_dto

    def get_day_wise_districts_cumulative_dto(self) -> DayWiseDistrictTotalCasesDtos:
        district_objs = District.objects.all(). \
             values('id', 'district_name', 'mandals__casesdetails__date'). \
             annotate(
                 total_confirmed_cases=Sum('mandals__casesdetails__confirmed_cases'),
                 total_recovered_cases=Sum('mandals__casesdetails__recovered_cases'),
                 total_deaths=Sum('mandals__casesdetails__deaths')
             )
        districts_ids = []
        districts_dates = []
        districts_objs_dict = defaultdict(lambda: {}) 
        for district in district_objs:
            id = district["id"]
            date = district["mandals__casesdetails__date"]
            districts_ids.append(id)
            districts_dates.append(date)
            districts_objs_dict[id][date] = district
        districts_dates = list(set(districts_dates))
        districts_ids = list(set(districts_ids))

        districts_dtos = self._get_day_wise_districts_cumulative_stats_dtos(
                district_objs, districts_ids, districts_dates, districts_objs_dict
            )
        districts_total_cases_dto = DayWiseDistrictTotalCasesDtos(
            districts=districts_dtos
        )
        return districts_total_cases_dto

    def _get_day_wise_districts_cumulative_stats_dtos(self, district_objs,
                                                districts_ids, districts_dates,
                                                districts_objs_dict):
        districts = []
        if not districts_dates:
            return districts
        date = min(districts_dates)
        max_date = max(districts_dates)
        delta = datetime.timedelta(days=1)

        for id in districts_ids:
            total_confirmed_cases = 0
            total_recovered_cases = 0
            total_deaths = 0
            day_wise_total_cases_dtos = []
            date = min(districts_dates)
            while date<=max_date:
                is_obj_present = self._is_obj_present(districts_objs_dict, id, date)
                if is_obj_present:
                    district = districts_objs_dict[id][date]
                    total_confirmed_cases += district["total_confirmed_cases"]
                    total_recovered_cases += district["total_recovered_cases"]
                    total_deaths += district["total_deaths"]
                day_wise_total_cases_dtos.append(
                    self._get_district_day_total_cases_dto(
                        total_confirmed_cases, total_recovered_cases,
                        total_deaths, date
                    )
                )
                date += delta
            districts.append(
                        self._get_day_wise_district_cumulative_dto(
                            day_wise_total_cases_dtos, id, district_objs
                        )
                    )
        return districts

    def _is_obj_present(self, districts_objs_dict, id, date):
        try:
            districts_objs_dict[id][date]
        except:
            return False
        return True

    def _get_district_day_total_cases_dto(
        self, total_confirmed_cases, total_recovered_cases, total_deaths, date):
        day_wise_total_cases_dto = DayWiseTotalCasesDto(
            date=date.strftime("%d/%m/%Y"),
            total_confirmed_cases=total_confirmed_cases,
            total_recovered_cases=total_recovered_cases,
            total_deaths=total_deaths
        )
        return day_wise_total_cases_dto

    def _get_day_wise_district_cumulative_dto(self, 
                                              day_wise_total_cases_dtos,
                                              id, district_objs):
        district_name = None
        for district in district_objs:
            if id == district["id"]:
                district_name = district["district_name"]
                break
        day_wise_district_dto = DayWiseDistrictTotalCasesDto(
            district_name=district_name,
            district_id=id,
            day_wise_statistics=day_wise_total_cases_dtos
        )
        return day_wise_district_dto

    def get_state_daily_details_dto(self, date: date) -> StateTotalCasesDto:
        state_dto = District.objects.filter(
            mandals__casesdetails__date=date,state_id=1). \
            values('state_id','state__state_name').annotate(
                total_confirmed_cases=Sum(
                    'mandals__casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'mandals__casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'mandals__casesdetails__deaths'
                )
            )
        districts_query_set = District.objects.filter(
            mandals__casesdetails__date=date). \
            values('id','district_name').annotate(
                total_confirmed_cases=Sum(
                    'mandals__casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'mandals__casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'mandals__casesdetails__deaths'
                )
            )
        if districts_query_set:
            state_total_cases_dto = self._get_state_total_cases_dto(state_dto, districts_query_set)
        else: 
           state_total_cases_dto = self._get_state_total_cases_dto_with_zeros()
        return state_total_cases_dto

    def get_day_wise_state_daily_dto(self, till_date: str) -> DayWiseStateTotalCasesDtos:
        district_details_objs = Mandal.objects.filter(
            casesdetails__date__lte=till_date
            ). \
            values('district__state_id', 'district__state__state_name', 'casesdetails__date'). \
            annotate(
                total_confirmed_cases=Sum('casesdetails__confirmed_cases'),
                total_recovered_cases=Sum('casesdetails__recovered_cases'),
                total_deaths=Sum('casesdetails__deaths')
            )

        dates = CasesDetails.objects.filter(date__lte=till_date).values_list('date', flat=True)
        dates_not_existed = not dates
        if dates_not_existed:
            state_name = State.objects.get(id=1).state_name
            day_wise_district_total_cases_dto = DayWiseStateTotalCasesDtos(
                    state_name=state_name,
                    day_wise_statistics=[]
            )
            return day_wise_district_total_cases_dto
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
        day_wise_district_total_cases_dto = DayWiseStateTotalCasesDtos(
                    state_name=district_details_objs[0]["district__state__state_name"],
                    day_wise_statistics=day_wise_statistics
        )
        return day_wise_district_total_cases_dto

    def get_districts_zones_dto(self) -> DistrictZones:
        state_dto = District.objects.filter(state_id=1). \
            values('state_id','state__state_name').annotate(
                total_confirmed_cases=Sum(
                    'mandals__casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'mandals__casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'mandals__casesdetails__deaths'
                )
            )
        districts_query_set = District.objects.filter(state_id=1). \
            values('id','district_name').annotate(
                total_confirmed_cases=Sum(
                    'mandals__casesdetails__confirmed_cases'
                ),
                total_recovered_cases=Sum(
                    'mandals__casesdetails__recovered_cases'
                ),
                total_deaths=Sum(
                    'mandals__casesdetails__deaths'
                )
            )
        state_total_active_cases = state_dto[0]["total_confirmed_cases"] - (
            state_dto[0]["total_recovered_cases"] + state_dto[0]["total_deaths"]
            )
        zone_dtos = []
        for district in districts_query_set:
            active_cases = district["total_confirmed_cases"] - (
            district["total_recovered_cases"] + district["total_deaths"]
            )
            percent = (100*(active_cases))/state_total_active_cases
            red_zone = percent >= 60
            orange_zone = percent >= 30 and percent < 60
            green_zone = percent < 30
            if red_zone:
                zone = "red_zone"
            if orange_zone:
                zone = "orange_zone"
            if green_zone:
                zone = "green_zone"
            district_zone_dto = Zone(
                district_id=district["id"],
                district_name=district["district_name"],
                zone=zone
            )
            zone_dtos.append(district_zone_dto)

        zones_dto = DistrictZones(
            zones = zone_dtos
        )
        return zones_dto





