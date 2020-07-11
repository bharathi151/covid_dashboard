from datetime import date
from dataclasses import dataclass
from typing import Optional, List


@dataclass()
class DayWiseStateCumulativeDto:
    date: str
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    total_active_cases: int

@dataclass()
class Zone:
    district_id: int
    district_name: str
    zone: str

@dataclass
class DistrictZones:
    zones: List[Zone]

@dataclass()
class DayWiseCumulativeDto:
    date: str
    total_recovered_cases: int
    total_confirmed_cases: int
    total_deaths: int
    total_active_cases: int

@dataclass()
class CasesDetailsDto:
    date: str
    mandal_id: int
    confirmed_cases: int
    recovered_cases: int
    deaths: int

@dataclass()
class PostCasesDetailsDto:
    date: str
    mandal_id: int
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int

# @dataclass()
# class UpdateCasesDetailsDto:
#     date: str
#     mandal_id: int
#     total_confirmed_cases: int
#     total_recovered_cases: int
#     total_deaths: int

@dataclass()
class DayStats:
    date: date
    district_name: str
    mandal_name: str
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    total_active_cases: int

@dataclass()
class StatsDtos:
    stats: List[DayStats]

@dataclass()
class DayWiseTotalCasesDto:
    date: str
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int

@dataclass()
class DayWiseDistrictTotalCasesDto:
    district_name: str
    district_id: int
    day_wise_statistics: List[DayWiseTotalCasesDto]

@dataclass()
class DayWiseMandalTotalCasesDto:
    mandal_name: str
    mandal_id: int
    day_wise_statistics: List[DayWiseTotalCasesDto]

@dataclass()
class DayWiseDistrictTotalCasesDtos:
    districts: List[DayWiseDistrictTotalCasesDto]

@dataclass()
class DayWiseMandalTotalCasesDtos:
    mandals : List[DayWiseMandalTotalCasesDto]

@dataclass()
class DayWiseDistrictCumulativeDto:
    district_name: str
    district_id: int
    day_wise_statistics: List[DayWiseCumulativeDto]

@dataclass()
class DayWiseMandalCumulativeDto:
    mandal_name: str
    mandal_id: int
    day_wise_statistics: List[DayWiseCumulativeDto]

@dataclass()
class DayWiseDistrictCumulativeDtos:
    districts: List[DayWiseDistrictCumulativeDto]

@dataclass()
class DayWiseMandalCumulativeDtos:
    mandals: List[DayWiseMandalCumulativeDto]

@dataclass()
class DayWiseStateTotalCasesDto:
    total_recovered_cases: int
    total_confirmed_cases: int
    total_deaths: int
    date: str

@dataclass()
class StateDto:
    state_name: str
    state_id: int

@dataclass()
class DistrictTotalCasesDto:
    district_name: str
    district_id: int
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int

@dataclass()
class MandalTotalCasesDto:
    mandal_name: str
    mandal_id: int
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int


@dataclass()
class StateTotalCasesDto:
    state_name: str
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    districts: List[DistrictTotalCasesDto]

@dataclass()
class DistrictTotalCasesDtos:
    district_name: str
    district_id: int
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    mandals: List[MandalTotalCasesDto]

@dataclass()
class MandalDto:
    mandal_name: str
    mandal_id: int
    district_id: int

@dataclass()
class DistrictDto:
    district_name: str
    district_id: int
    state_id: int

@dataclass()
class DayWiseStateCumulativeDtos:
    state_name: str
    day_wise_statistics: List[DayWiseStateCumulativeDto]


@dataclass()
class DayWiseStateTotalCasesDtos:
    state_name: str
    day_wise_statistics: List[DayWiseStateTotalCasesDto]

@dataclass()
class StateCumulativeDto:
    state_name: str
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    total_active_cases: int


@dataclass()
class DistrictCumulativeDto:
    district_name: str
    district_id: int
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    total_active_cases: int

@dataclass()
class MandalCumulativeDto:
    mandal_name: str
    mandal_id: int
    total_confirmed_cases: int
    total_recovered_cases: int
    total_deaths: int
    total_active_cases: int

@dataclass()
class StateCumulativeDtos:
    state: StateCumulativeDto
    districts: List[DistrictCumulativeDto]

@dataclass()
class DistrictCumulativeDtos:
    district: DistrictCumulativeDto
    mandals: List[MandalCumulativeDto]