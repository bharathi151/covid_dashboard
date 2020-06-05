# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "post_cases_deatils"
REQUEST_METHOD = "post"
URL_SUFFIX = "{mandal_id}/post_cases/v1/"

from .test_case_01 import TestCase01PostCasesDeatilsAPITestCase

__all__ = [
    "TestCase01PostCasesDeatilsAPITestCase"
]
