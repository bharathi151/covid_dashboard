# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_cumulative_report_day_wise"
REQUEST_METHOD = "get"
URL_SUFFIX = "district/{district_id}/cumulative/day_wise/report/v1/"

from .test_case_01 import TestCase01GetDistrictCumulativeReportDayWiseAPITestCase

__all__ = [
    "TestCase01GetDistrictCumulativeReportDayWiseAPITestCase"
]
