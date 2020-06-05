# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_districts_daily_report_day_wise"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/daily/day_wise/report/v1/"

from .test_case_01 import TestCase01GetDistrictsDailyReportDayWiseAPITestCase

__all__ = [
    "TestCase01GetDistrictsDailyReportDayWiseAPITestCase"
]
