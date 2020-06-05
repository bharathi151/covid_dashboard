# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "sign_in_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "sign_in/v1/"

from .test_case_01 import TestCase01SignInUserAPITestCase

__all__ = [
    "TestCase01SignInUserAPITestCase"
]
