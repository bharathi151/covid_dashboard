# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_state_cumulative_report_day_wise"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/cumulative/day_wise/report/v1/"

from .test_case_01 import TestCase01GetStateCumulativeReportDayWiseAPITestCase

__all__ = [
    "TestCase01GetStateCumulativeReportDayWiseAPITestCase"
]
