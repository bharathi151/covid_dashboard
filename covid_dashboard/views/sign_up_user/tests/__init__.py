# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "sign_up_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "sign_up/v1/"

from .test_case_01 import TestCase01SignUpUserAPITestCase

__all__ = [
    "TestCase01SignUpUserAPITestCase"
]
