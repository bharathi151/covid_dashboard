# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_daily_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "district/{district_id}/daily/report/v1/"

from .test_case_01 import TestCase01GetDistrictDailyReportAPITestCase

__all__ = [
    "TestCase01GetDistrictDailyReportAPITestCase"
]
