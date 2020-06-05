# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_state_daily_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/daily/report/v1/"

from .test_case_01 import TestCase01GetStateDailyReportAPITestCase

__all__ = [
    "TestCase01GetStateDailyReportAPITestCase"
]
