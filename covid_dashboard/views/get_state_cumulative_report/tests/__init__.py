# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_state_cumulative_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/cumulative/report/v1/"

from .test_case_01 import TestCase01GetStateCumulativeReportAPITestCase

__all__ = [
    "TestCase01GetStateCumulativeReportAPITestCase"
]
