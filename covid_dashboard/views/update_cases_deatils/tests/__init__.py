# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "update_cases_deatils"
REQUEST_METHOD = "post"
URL_SUFFIX = "{mandal_id}/update_cases/v1/"

from .test_case_01 import TestCase01UpdateCasesDeatilsAPITestCase

__all__ = [
    "TestCase01UpdateCasesDeatilsAPITestCase"
]
