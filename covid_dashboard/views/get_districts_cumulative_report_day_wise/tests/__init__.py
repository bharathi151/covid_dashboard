# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_districts_cumulative_report_day_wise"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/cumulative/day_wise/report/v1/"

from .test_case_01 import TestCase01GetDistrictsCumulativeReportDayWiseAPITestCase

__all__ = [
    "TestCase01GetDistrictsCumulativeReportDayWiseAPITestCase"
]
