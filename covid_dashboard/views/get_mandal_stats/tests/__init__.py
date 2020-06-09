# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_mandal_stats"
REQUEST_METHOD = "get"
URL_SUFFIX = "mandals_stats/v1/"

from .test_case_01 import TestCase01GetMandalStatsAPITestCase

__all__ = [
    "TestCase01GetMandalStatsAPITestCase"
]
