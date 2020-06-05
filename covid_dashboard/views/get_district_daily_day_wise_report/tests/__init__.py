# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_daily_day_wise_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "district/{district_id}/daily/day_wise/report/v1/"

from .test_case_01 import TestCase01GetDistrictDailyDayWiseReportAPITestCase

__all__ = [
    "TestCase01GetDistrictDailyDayWiseReportAPITestCase"
]
