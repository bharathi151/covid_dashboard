# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_districts_zones"
REQUEST_METHOD = "get"
URL_SUFFIX = "get_districts_zones/v1/"

from .test_case_01 import TestCase01GetDistrictsZonesAPITestCase

__all__ = [
    "TestCase01GetDistrictsZonesAPITestCase"
]
